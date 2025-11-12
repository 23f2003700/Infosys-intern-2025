"""
Deploy BioGPT on Amazon SageMaker as FREE backup GenAI model
Uses HuggingFace microsoft/BioGPT-Large for medical text generation
"""
import boto3
import sagemaker
from sagemaker.huggingface import HuggingFaceModel
import json

def deploy_biogpt():
    """
    Deploy BioGPT-Large from HuggingFace to SageMaker endpoint
    Instance: ml.m5.xlarge (4 vCPU, 16 GB RAM)
    Model: microsoft/BioGPT-Large (1.5B parameters)
    """
    print("🚀 Deploying BioGPT to Amazon SageMaker...")
    
    # Get AWS account and region
    sts = boto3.client('sts')
    account_id = sts.get_caller_identity()['Account']
    region = boto3.Session().region_name or 'us-east-1'
    
    print(f"📍 Account: {account_id}, Region: {region}")
    
    # Check if SageMaker execution role exists, create if not
    iam = boto3.client('iam')
    role_name = 'sagemaker-execution-role'
    
    try:
        role = iam.get_role(RoleName=role_name)
        role_arn = role['Role']['Arn']
        print(f"✅ Using existing role: {role_arn}")
    except iam.exceptions.NoSuchEntityException:
        print(f"⚠️  Role {role_name} not found. Creating...")
        
        # Create trust policy for SageMaker
        trust_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "sagemaker.amazonaws.com"},
                    "Action": "sts:AssumeRole"
                }
            ]
        }
        
        role = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description='Execution role for SageMaker BioGPT deployment'
        )
        role_arn = role['Role']['Arn']
        
        # Attach necessary policies
        iam.attach_role_policy(
            RoleName=role_name,
            PolicyArn='arn:aws:iam::aws:policy/AmazonSageMakerFullAccess'
        )
        iam.attach_role_policy(
            RoleName=role_name,
            PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
        )
        
        print(f"✅ Created role: {role_arn}")
        print("⏳ Waiting 10 seconds for role to propagate...")
        import time
        time.sleep(10)
    
    # Configure HuggingFace model
    hub_config = {
        'HF_MODEL_ID': 'microsoft/BioGPT-Large',  # 1.5B parameter medical LLM
        'HF_TASK': 'text-generation'
    }
    
    print(f"📦 Model: {hub_config['HF_MODEL_ID']}")
    print(f"🎯 Task: {hub_config['HF_TASK']}")
    
    # Create HuggingFace Model
    huggingface_model = HuggingFaceModel(
        transformers_version='4.26.0',  # Stable version compatible with BioGPT
        pytorch_version='1.13.1',       # Compatible PyTorch version
        py_version='py39',              # Python 3.9
        env=hub_config,
        role=role_arn,
        name='biogpt-medical-model'
    )
    
    print("🔧 Model configuration created")
    
    # Deploy to SageMaker endpoint
    endpoint_name = 'biogpt-medical-endpoint'
    instance_type = 'ml.m5.xlarge'  # 4 vCPU, 16 GB RAM - suitable for BioGPT-Large
    
    print(f"🚢 Deploying to endpoint: {endpoint_name}")
    print(f"💻 Instance type: {instance_type}")
    print("⏳ This will take 5-10 minutes...")
    
    try:
        predictor = huggingface_model.deploy(
            initial_instance_count=1,
            instance_type=instance_type,
            endpoint_name=endpoint_name
        )
        
        print("✅ Deployment successful!")
        print(f"🎉 Endpoint: {endpoint_name}")
        print(f"🔗 Endpoint ARN: arn:aws:sagemaker:{region}:{account_id}:endpoint/{endpoint_name}")
        
        # Test the endpoint
        print("\n🧪 Testing endpoint with medical text...")
        test_input = {
            "inputs": "Patient presents with severe chest pain and shortness of breath.",
            "parameters": {
                "max_new_tokens": 100,
                "temperature": 0.7,
                "top_p": 0.9
            }
        }
        
        response = predictor.predict(test_input)
        print(f"📝 Test response: {response}")
        
        return {
            'endpoint_name': endpoint_name,
            'endpoint_arn': f"arn:aws:sagemaker:{region}:{account_id}:endpoint/{endpoint_name}",
            'instance_type': instance_type,
            'model_id': hub_config['HF_MODEL_ID'],
            'status': 'InService'
        }
        
    except Exception as e:
        print(f"❌ Deployment failed: {str(e)}")
        raise

def test_biogpt_endpoint(endpoint_name='biogpt-medical-endpoint'):
    """Test existing BioGPT endpoint"""
    import sagemaker
    from sagemaker.predictor import Predictor
    from sagemaker.serializers import JSONSerializer
    from sagemaker.deserializers import JSONDeserializer
    
    predictor = Predictor(
        endpoint_name=endpoint_name,
        serializer=JSONSerializer(),
        deserializer=JSONDeserializer()
    )
    
    test_cases = [
        "Patient with diabetes and hypertension",
        "Chest pain radiating to left arm",
        "Fever, cough, and difficulty breathing"
    ]
    
    print(f"\n🧪 Testing endpoint: {endpoint_name}\n")
    
    for i, test_text in enumerate(test_cases, 1):
        print(f"Test {i}: {test_text}")
        response = predictor.predict({
            "inputs": test_text,
            "parameters": {"max_new_tokens": 50, "temperature": 0.7}
        })
        print(f"Response: {response}\n")

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Deploy BioGPT to SageMaker')
    parser.add_argument('--test-only', action='store_true', help='Test existing endpoint')
    args = parser.parse_args()
    
    if args.test_only:
        test_biogpt_endpoint()
    else:
        result = deploy_biogpt()
        print(f"\n📊 Deployment Summary:")
        print(json.dumps(result, indent=2))
        print("\n💡 Add this to Lambda environment variables:")
        print(f"SAGEMAKER_ENDPOINT={result['endpoint_name']}")
