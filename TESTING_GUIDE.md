# 🧪 Testing Guide - EHR AI System Validation

## Quick Test URLs

**Live Application**: http://ehr-frontend-48208.s3-website-us-east-1.amazonaws.com  
**API Endpoint**: https://cvu4o3ywpl.execute-api.us-east-1.amazonaws.com/prod  
**GitHub**: https://github.com/23f2003700/Infosys-intern-2025

---

## ✅ Test 1: Clinical Notes Generation with Valid Input

**Navigate to**: http://ehr-frontend-48208.s3-website-us-east-1.amazonaws.com/clinical-notes

**Input**:
```
Patient Name: John Smith
Age: 58
Gender: Male
Chief Complaint: Chest Pain

Clinical Findings:
Patient presents to the emergency department with acute onset chest pain radiating to the left arm. Pain described as crushing, 8/10 severity. Associated symptoms include shortness of breath, diaphoresis, and nausea. 

Vital Signs:
- BP: 165/95 mmHg (elevated)
- HR: 102 bpm (tachycardia)
- Temp: 98.6°F
- SpO2: 94% on room air

Physical Examination:
Heart sounds regular, no murmurs. Lung sounds clear bilaterally. Mild diaphoresis noted. No peripheral edema.

Medical History:
- Hypertension (5 years)
- Type 2 Diabetes Mellitus (3 years)
- Hyperlipidemia
- Former smoker (quit 2 years ago)
```

**Expected Result**: ✅ Should generate professional SOAP note with all sections
- UI should show "Amazon Titan GenAI (FREE)" badge (green)
- Button should say "Generate with AI" (not "Generate with Claude 3")
- Generated note should include Subjective, Objective, Assessment, Plan sections

---

## ❌ Test 2: Clinical Notes with Invalid Input (Gibberish)

**Navigate to**: http://ehr-frontend-48208.s3-website-us-east-1.amazonaws.com/clinical-notes

**Input**:
```
Patient Name: ab
Age: 25
Gender: Male
Chief Complaint: Random text

Clinical Findings:
asdfgh jklqwe zxcvbn mnbvcx lkjhgf poiuyt rewqas dfghjk
```

**Expected Result**: ❌ Should reject with error message
- Error: "Invalid input: Patient name is required and must be at least 2 characters"
- OR Error: "Invalid input: Input does not appear to contain valid medical/clinical information"
- Should NOT generate any clinical note
- Should display clear error message to user

---

## ❌ Test 3: Clinical Notes with Non-Medical Text

**Navigate to**: http://ehr-frontend-48208.s3-website-us-east-1.amazonaws.com/clinical-notes

**Input**:
```
Patient Name: Test User
Age: 30
Gender: Female
Chief Complaint: Nothing specific

Clinical Findings:
The quick brown fox jumps over the lazy dog. Lorem ipsum dolor sit amet, consectetur adipiscing elit. This is just random text with no medical content whatsoever.
```

**Expected Result**: ❌ Should reject with error message
- Error: "Invalid input: Input does not appear to contain valid medical/clinical information"
- Validation checks for medical keywords: pain, fever, symptom, diagnosis, etc.
- Should NOT accept non-medical text

---

## ✅ Test 4: ICD-10 Coding with Valid Input

**Navigate to**: http://ehr-frontend-48208.s3-website-us-east-1.amazonaws.com/icd10-coding

**Input**:
```
Patient is a 62-year-old male with history of hypertension and type 2 diabetes mellitus presenting with acute myocardial infarction. Patient experienced severe chest pain, elevated troponin levels, and ECG changes consistent with ST-elevation MI. Also has chronic kidney disease stage 3 and hyperlipidemia.
```

**Expected Result**: ✅ Should suggest relevant ICD-10 codes
- UI should show "Amazon Titan GenAI (FREE)" badge (green, not blue)
- Should NOT mention "Powered by Claude 3"
- Should return codes like:
  - I21.9 (Acute myocardial infarction)
  - I10 (Essential hypertension)
  - E11.9 (Type 2 diabetes mellitus)
  - N18.3 (Chronic kidney disease, stage 3)
  - E78.5 (Hyperlipidemia)

---

## ❌ Test 5: ICD-10 Coding with Invalid Input

**Navigate to**: http://ehr-frontend-48208.s3-website-us-east-1.amazonaws.com/icd10-coding

**Input**:
```
xyz abc qwe rty uio
```

**Expected Result**: ❌ Should reject with error message
- Error: "Invalid input: Clinical text must be at least 15 characters long"
- OR Error: "Input does not appear to contain valid medical/clinical information"
- Should validate for medical content before calling AI

---

## ❌ Test 6: ICD-10 Coding with Too Many Special Characters

**Navigate to**: http://ehr-frontend-48208.s3-website-us-east-1.amazonaws.com/icd10-coding

**Input**:
```
!@#$%^&*()_+{}|:"<>?[]\'
```

**Expected Result**: ❌ Should reject with error message
- Error: "Input contains too many invalid characters. Please provide clear clinical text."
- Validation checks that at least 60% of characters are alphabetic

---

## 🎨 Test 7: UI Branding Verification

**Check all pages**:

1. **Clinical Notes Page**:
   - ✅ Button should say "Generate with AI" (gradient green)
   - ✅ Badge should say "Amazon Titan GenAI (FREE)" (green color)
   - ✅ Description should mention "Amazon Titan Text Express"
   - ❌ Should NOT mention "Claude 3" anywhere
   - ❌ Should NOT mention "Powered by Amazon Bedrock" with Claude

2. **ICD-10 Coding Page**:
   - ✅ Badge should say "Amazon Titan GenAI (FREE)" (green color)
   - ❌ Should NOT say "Powered by Claude 3"
   - ✅ Badge color should be green (success), not blue (info)

---

## 🔧 Test 8: Lambda Function Validation (Backend)

**Test via AWS Console or CLI**:

### Test Clinical Notes Lambda:
```bash
aws lambda invoke \
  --function-name ehr-clinical-notes \
  --payload '{"patient_info": {"name": "Test", "age": 30}, "findings": "asdfgh jkl"}' \
  --region us-east-1 \
  response.json

cat response.json
```

**Expected**: Should return error with validation message

### Test ICD-10 Lambda:
```bash
aws lambda invoke \
  --function-name ehr-icd10-coding \
  --payload '{"clinical_text": "xyz"}' \
  --region us-east-1 \
  response.json

cat response.json
```

**Expected**: Should return error with validation message

---

## 🚀 Test 9: SageMaker BioGPT Deployment (Optional)

**Deploy BioGPT**:
```bash
cd backend
pip install sagemaker boto3
python deploy_sagemaker_biogpt.py
```

**Expected Output**:
```
🚀 Deploying BioGPT to Amazon SageMaker...
📍 Account: 340663646697, Region: us-east-1
✅ Using existing role: arn:aws:iam::...
📦 Model: microsoft/BioGPT-Large
🎯 Task: text-generation
🔧 Model configuration created
🚢 Deploying to endpoint: biogpt-medical-endpoint
💻 Instance type: ml.m5.xlarge
⏳ This will take 5-10 minutes...
✅ Deployment successful!
🎉 Endpoint: biogpt-medical-endpoint
```

**Test Endpoint**:
```bash
python deploy_sagemaker_biogpt.py --test-only
```

**Add to Lambda**:
```bash
aws lambda update-function-configuration \
  --function-name ehr-clinical-notes \
  --environment "Variables={BEDROCK_MODEL_ID=amazon.titan-text-express-v1,SAGEMAKER_ENDPOINT=biogpt-medical-endpoint,DYNAMODB_TABLE_NAME=ehr-patient-records}" \
  --region us-east-1
```

---

## 📊 Validation Checklist

| Test Case | Category | Status | Notes |
|-----------|----------|--------|-------|
| Valid clinical text | Clinical Notes | ⏳ Test | Should generate SOAP note |
| Gibberish input (short name) | Clinical Notes | ⏳ Test | Should reject |
| Non-medical text | Clinical Notes | ⏳ Test | Should reject |
| Valid ICD-10 input | ICD-10 Coding | ⏳ Test | Should suggest codes |
| Invalid ICD-10 input | ICD-10 Coding | ⏳ Test | Should reject |
| Special characters only | ICD-10 Coding | ⏳ Test | Should reject |
| UI shows "Claude 3" | UI Branding | ✅ Fixed | No Claude references |
| UI shows Amazon Titan | UI Branding | ✅ Fixed | Green theme |
| Lambda validation works | Backend | ✅ Deployed | 8.4 KB package |
| SageMaker fallback | Backend | ⏳ Optional | Deploy script ready |

---

## 🔍 How to Check Validation Logic

### Clinical Notes Validation (35 Medical Keywords):
```python
# These words MUST be in clinical findings for validation to pass:
pain, symptom, fever, cough, headache, fatigue, nausea, chest, abdomen, 
throat, temperature, pressure, heart, lung, breathing, dizzy, swelling, 
rash, injury, fracture, diagnosis, patient, medical, treatment, medication, 
history, examination, vital, blood, pulse, respiratory, bp, hr, complaint
```

### ICD-10 Coding Validation (29 Medical Keywords):
```python
# These words MUST be in clinical text for validation to pass:
patient, diagnosis, symptom, condition, disease, pain, fever, cough, blood, 
pressure, diabetes, hypertension, heart, kidney, liver, lung, chronic, acute, 
treatment, medication, injury, fracture, infection, inflammation, presents, 
complaints, history, examination, findings
```

---

## ⚠️ Known Issues

1. **HTTPS Not Available**:
   - CloudFront deployment failed (IAM permissions)
   - Currently using HTTP only: http://ehr-frontend-48208.s3-website-us-east-1.amazonaws.com
   - Workaround: Manual CloudFront setup (see CLOUDFRONT_SETUP.md)

2. **SageMaker BioGPT Not Deployed**:
   - Deployment script ready: `backend/deploy_sagemaker_biogpt.py`
   - Requires `pip install sagemaker`
   - Lambda fallback code already added (will use if SAGEMAKER_ENDPOINT env var set)

---

## 📞 Support

**Issues**: https://github.com/23f2003700/Infosys-intern-2025/issues  
**Live Demo**: http://ehr-frontend-48208.s3-website-us-east-1.amazonaws.com  
**API Docs**: See README.md

**Last Updated**: December 12, 2024
