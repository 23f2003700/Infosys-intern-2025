"""
AWS Lambda Function: ICD-10 Code Suggestion
Uses Amazon Bedrock Titan Text Express (FREE) for intelligent medical coding
"""
import json
import boto3
import os
import re

# Initialize Bedrock client
bedrock_runtime = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))

# Common ICD-10 codes reference
ICD10_REFERENCE = {
    'I10': 'Essential (primary) hypertension',
    'E11.9': 'Type 2 diabetes mellitus without complications',
    'J44.9': 'Chronic obstructive pulmonary disease, unspecified',
    'I25.10': 'Atherosclerotic heart disease of native coronary artery without angina pectoris',
    'F41.9': 'Anxiety disorder, unspecified',
    'M79.3': 'Panniculitis, unspecified',
    'K21.9': 'Gastro-esophageal reflux disease without esophagitis',
    'N18.9': 'Chronic kidney disease, unspecified',
    'E78.5': 'Hyperlipidemia, unspecified',
    'I50.9': 'Heart failure, unspecified'
}

def validate_clinical_text(clinical_text):
    """
    Validate that input contains valid clinical/medical information
    Returns: (is_valid, error_message)
    """
    if not clinical_text or len(clinical_text.strip()) < 15:
        return False, "Clinical text must be at least 15 characters long"
    
    # Check for medical keywords to ensure it's clinical text
    medical_keywords = [
        'patient', 'diagnosis', 'symptom', 'condition', 'disease', 'pain', 
        'fever', 'cough', 'blood', 'pressure', 'diabetes', 'hypertension',
        'heart', 'kidney', 'liver', 'lung', 'chronic', 'acute', 'treatment',
        'medication', 'injury', 'fracture', 'infection', 'inflammation',
        'presents', 'complaints', 'history', 'examination', 'findings'
    ]
    
    text_lower = clinical_text.lower()
    has_medical_content = any(keyword in text_lower for keyword in medical_keywords)
    
    if not has_medical_content:
        return False, "Input does not appear to contain valid medical/clinical information. Please provide relevant clinical documentation."
    
    # Check if input is mostly gibberish (too many non-alphabetic characters)
    alpha_chars = sum(c.isalpha() or c.isspace() for c in clinical_text)
    if alpha_chars / len(clinical_text) < 0.6:
        return False, "Input contains too many invalid characters. Please provide clear clinical text."
    
    return True, None

def suggest_icd10_codes(clinical_text, bedrock_client, top_k=5):
    """
    Use Amazon Titan Text Express (FREE GenAI) to suggest ICD-10 codes from clinical text
    With SageMaker BioGPT fallback for resilience
    """
    # Validate input first
    is_valid, error_msg = validate_clinical_text(clinical_text)
    if not is_valid:
        raise ValueError(f"Invalid input: {error_msg}")
    
    model_id = os.environ.get('BEDROCK_MODEL_ID', 'amazon.titan-text-express-v1')
    sagemaker_endpoint = os.environ.get('SAGEMAKER_ENDPOINT')
    
    prompt = f"""You are an expert medical coder. Analyze the following clinical text and suggest the most appropriate ICD-10 codes.

Clinical Text:
{clinical_text}

ICD-10 Code Reference:
{json.dumps(ICD10_REFERENCE, indent=2)}

Provide the top {top_k} most relevant ICD-10 codes in JSON format with:
- code: The ICD-10 code
- description: Full description
- confidence: Confidence score (0-1)
- reasoning: Brief explanation why this code applies

Format your response as a valid JSON array."""

    try:
        # Primary: Amazon Titan Text Express (FREE)
        request_body = {
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 2000,
                "temperature": 0.1,  # Low temperature for more deterministic results
                "topP": 0.9,
                "stopSequences": []
            }
        }
        
        response = bedrock_client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )
        
        response_body = json.loads(response['body'].read())
        response_text = response_body['results'][0]['outputText']
        
    except Exception as bedrock_error:
        # Fallback: SageMaker BioGPT if Bedrock fails
        if sagemaker_endpoint:
            print(f"⚠️ Bedrock failed, trying SageMaker BioGPT: {str(bedrock_error)}")
            sagemaker_runtime = boto3.client('sagemaker-runtime')
            
            response = sagemaker_runtime.invoke_endpoint(
                EndpointName=sagemaker_endpoint,
                ContentType='application/json',
                Body=json.dumps({
                    "inputs": prompt,
                    "parameters": {
                        "max_new_tokens": 500,
                        "temperature": 0.1,
                        "top_p": 0.9
                    }
                })
            )
            
            result = json.loads(response['Body'].read())
            response_text = result[0]['generated_text'] if isinstance(result, list) else result['generated_text']
        else:
            raise bedrock_error
    
    # Extract JSON from response
    try:
        # Try to parse the entire response as JSON
        codes = json.loads(response_text)
    except:
        # If that fails, try to extract JSON array from markdown code blocks
        json_match = re.search(r'```json\s*(.*?)\s*```', response_text, re.DOTALL)
        if json_match:
            codes = json.loads(json_match.group(1))
        else:
            # Try to find JSON array in the text
            json_match = re.search(r'\[\s*{.*}\s*\]', response_text, re.DOTALL)
            if json_match:
                codes = json.loads(json_match.group(0))
            else:
                codes = []
    
    return codes

def validate_icd10_code(code):
    """
    Validate ICD-10 code format
    """
    # Basic ICD-10 format validation
    pattern = r'^[A-Z][0-9]{2}\.?[0-9A-Z]{0,4}$'
    return bool(re.match(pattern, code.upper()))

def get_code_details(code):
    """
    Get details for a specific ICD-10 code
    """
    # Check if code exists in reference
    if code in ICD10_REFERENCE:
        return {
            'code': code,
            'description': ICD10_REFERENCE[code],
            'valid': True
        }
    else:
        return {
            'code': code,
            'description': 'Code not in reference database',
            'valid': validate_icd10_code(code)
        }

def lambda_handler(event, context):
    """
    AWS Lambda handler for ICD-10 code suggestion
    """
    try:
        # Parse request
        body = json.loads(event.get('body', '{}'))
        clinical_text = body.get('clinical_text', '')
        top_k = body.get('top_k', 5)
        
        if not clinical_text:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'Missing clinical_text'})
            }
        
        # Get ICD-10 suggestions from Bedrock
        suggested_codes = suggest_icd10_codes(clinical_text, bedrock_runtime, top_k)
        
        # Validate and enrich codes
        validated_codes = []
        for code_item in suggested_codes:
            code = code_item.get('code', '')
            code_details = get_code_details(code)
            
            validated_codes.append({
                'code': code,
                'description': code_item.get('description', code_details['description']),
                'confidence': code_item.get('confidence', 0.0),
                'reasoning': code_item.get('reasoning', ''),
                'valid': code_details['valid']
            })
        
        # Sort by confidence
        validated_codes.sort(key=lambda x: x['confidence'], reverse=True)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'clinical_text': clinical_text,
                'suggested_codes': validated_codes[:top_k],
                'total_suggestions': len(validated_codes),
                'model': 'claude-3-sonnet',
                'success': True
            })
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e),
                'success': False
            })
        }
