# 🏥 EHR AI System
> AI-Powered Imaging & Intelligent Clinical Documentation Platform

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688.svg)](https://fastapi.tiangolo.com/)
[![React 18](https://img.shields.io/badge/React-18.2-61dafb.svg)](https://react.dev/)
[![PyTorch 2.0+](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C.svg)](https://pytorch.org/)
[![Azure OpenAI](https://img.shields.io/badge/Azure-OpenAI-0089D6.svg)](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
[![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900.svg)](https://aws.amazon.com/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)](#-project-status)
[![License](https://img.shields.io/badge/License-Infosys%20Internship-lightgrey.svg)](#-license)

---

## 📌 Overview

A production-ready Electronic Health Record (EHR) AI platform that combines:
- Generative AI for clinical documentation
- Deep learning–powered medical image enhancement
- Automated ICD-10 coding
- Secure patient management

Built with React, FastAPI, AWS Lambda, Amazon Bedrock (Titan), Azure OpenAI (GPT‑4 Vision), DynamoDB, and U‑Net/BioBERT models.

Author: Aaryan Choudhary  
Program: Infosys Springboard Internship 2025  
Email: rampyaaryan17@gmail.com

---

## 🔗 Live Resources

| Component | URL |
|----------|-----|
| Frontend (S3) | http://ehr-frontend-48208.s3-website-us-east-1.amazonaws.com |
| Public API (Prod) | https://cvu4o3ywpl.execute-api.us-east-1.amazonaws.com/prod |
| GitHub Repo | https://github.com/23f2003700/Infosys-intern-2025 |
| Issue Tracker | https://github.com/23f2003700/Infosys-intern-2025/issues |

> Note: Accessing the API root path returns {"message":"Missing Authentication Token"} by design. Use explicit endpoints (see API Endpoints).

---

## 📚 Table of Contents
1. [Key Features](#-key-features)
2. [Project Structure & Workflow](#-project-structure--workflow)
3. [Architecture](#-architecture)
4. [Technology Stack](#-technology-stack)
5. [Quick Start](#-quick-start)
6. [API Endpoints](#-api-endpoints)
7. [Configuration](#-configuration)
8. [Security & Compliance](#-security--compliance)
9. [Performance Metrics](#-performance-metrics)
10. [Training & Notebooks](#-training--notebooks)
11. [Testing](#-testing)
12. [Troubleshooting](#-troubleshooting)
13. [Future Enhancements](#-future-enhancements)
14. [Contributing](#-contributing)
15. [Project Status](#-project-status)
16. [Acknowledgments](#-acknowledgments)
17. [Contact](#-contact)
18. [License](#-license)

---

## ✨ Key Features

### 🖼 Medical Imaging Enhancement
- Multi-modality: X-ray, CT, MRI, Ultrasound, DXA
- Classic pipeline: NLM denoising, CLAHE, sharpening, edge enhancement
- Deep Learning: U‑Net (31M params) with PSNR/SSIM evaluation
- Batch workflows with side-by-side visual comparisons

### 📝 Automated Clinical Documentation
- SOAP notes, progress notes, discharge summaries, radiology reports
- Hybrid LLM strategy: Amazon Titan Text + Azure OpenAI GPT‑4 Vision
- Medical terminology extraction and guardrails

### 🏷 ICD‑10 Coding Assistant
- AI-assisted multi-label code suggestions with confidence scores
- BioBERT / BioGPT fine-tuning compatible
- Includes common diagnostic codes (I10, E11.9, J44.9, I25.10, etc.)

### 👥 Patient Management
- CRUD for patient records (DynamoDB)
- Demographic and history tracking
- Built-in anonymization utilities

### 🔐 Security & Validation
- 35+ medical keyword validation, gibberish detection
- Strict input schema checks (name, age, text length)
- IAM least-privilege, S3/DynamoDB encryption, API throttling

---

## 🧭 Project Structure & Workflow

### Directory Structure

```
ehr-ai-system/
│
├── frontend/                           # React Frontend Application
│   ├── public/                        # Static assets
│   ├── src/
│   │   ├── components/                # Reusable React components
│   │   ├── pages/                     # Main application pages
│   │   │   ├── Dashboard.jsx          # Main dashboard
│   │   │   ├── ImageEnhancement.jsx   # Medical image enhancement UI
│   │   │   ├── ClinicalNotes.jsx      # Clinical documentation UI
│   │   │   ├── ICD10Coding.jsx        # ICD-10 coding assistant UI
│   │   │   └── PatientManagement.jsx  # Patient records management
│   │   ├── services/                  # API service layer
│   │   │   └── api.js                 # Axios API client
│   │   ├── App.jsx                    # Main application component
│   │   ├── main.jsx                   # React entry point
│   │   └── index.css                  # Global styles
│   ├── .env.production                # Production environment variables
│   ├── package.json                   # NPM dependencies
│   ├── vite.config.js                 # Vite build configuration
│   └── dist/                          # Build output (deployed to S3)
│
├── backend/
│   ├── lambda_functions/              # AWS Lambda function code
│   │   ├── clinical_notes_generator.py    # SOAP notes generation
│   │   ├── icd10_coding.py                # ICD-10 code suggestion
│   │   └── image_enhancement.py           # Medical image enhancement
│   ├── deploy_sagemaker_biogpt.py     # SageMaker BioGPT deployment script
│   └── requirements-lambda.txt        # Lambda dependencies
│
├── infrastructure/
│   ├── cloudformation-template.yaml   # Main CloudFormation stack
│   ├── cloudfront-template.yaml       # HTTPS CloudFront setup
│   ├── packaged-template.yaml         # Packaged Lambda deployment
│   └── pure-cloudformation.yaml       # Alternative deployment template
│
├── src/                               # Original source modules
│   ├── module1_data_preprocessing/    # Data preprocessing utilities
│   ├── module2_image_enhancement/     # Image enhancement algorithms
│   ├── module3_documentation_automation/  # NLP for documentation
│   └── module4_integration/           # Integration utilities
│
├── config/
│   └── config.yaml                    # Application configuration
│
├── data/
│   ├── raw/                           # Raw medical images
│   │   ├── xray/
│   │   ├── ct/
│   │   ├── mri/
│   │   ├── ultrasound/
│   │   └── dxa/
│   ├── processed/                     # Processed training data
│   └── output/                        # Enhancement results
│
├── models/                            # Trained ML models (if any)
│   ├── clinical_notes/
│   ├── icd10_coding/
│   └── image_enhancement/
│
├── notebooks/                         # Jupyter notebooks for development
│   ├── 01_image_enhancement_training.ipynb
│   ├── 02_clinical_nlp_training.ipynb
│   └── 03_system_testing.ipynb
│
├── tests/                             # Unit and integration tests
│   ├── test_module1.py
│   └── test_module2.py
│
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
└── pytest.ini                         # Test configuration
```

### System Workflow

```
User Browser
    ↓
Frontend (React on S3)
http://ehr-frontend-48208.s3-website-us-east-1.amazonaws.com
    ↓
API Gateway (Prod)
https://cvu4o3ywpl.execute-api.us-east-1.amazonaws.com/prod
    ↓
AWS Lambda Functions
    ↓
Amazon Bedrock (Titan Text) + DynamoDB + S3
```

#### Frontend Architecture

- React 18.2 + Vite + MUI v5
- React Router for navigation
- Axios for API calls

```javascript
// frontend/src/services/api.js
import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_URL; // e.g., https://cvu4o3ywpl.execute-api.us-east-1.amazonaws.com/prod

export const generateNotes = (payload) =>
  axios.post(`${API_BASE}/generate-notes`, payload);

export const suggestICD10 = (payload) =>
  axios.post(`${API_BASE}/suggest-icd10`, payload);

export const enhanceImage = (payload) =>
  axios.post(`${API_BASE}/enhance-image`, payload);
```

#### Backend Architecture

AWS Lambda functions:

1. ehr-clinical-notes
   - Handler: clinical_notes_generator.lambda_handler
   - Runtime: Python 3.11
   - Memory: 1024 MB
   - Timeout: 60s
   - Purpose: Generate SOAP notes via Amazon Titan

2. ehr-icd10-coding
   - Handler: icd10_coding.lambda_handler
   - Runtime: Python 3.11
   - Memory: 512 MB
   - Timeout: 30s
   - Purpose: Suggest ICD‑10 codes

3. ehr-image-enhancement
   - Handler: image_enhancement.lambda_handler
   - Runtime: Python 3.11
   - Memory: 1024 MB
   - Timeout: 60s
   - Purpose: Enhance medical images

API Gateway endpoints:

```
GET  /prod/                          → Returns "Missing Authentication Token" (expected)
POST /prod/generate-notes            → Clinical notes generation
POST /prod/suggest-icd10             → ICD-10 code suggestion
POST /prod/enhance-image             → Image enhancement
POST /prod/patients                  → Create patient record
GET  /prod/patients/{id}             → Get patient record
PUT  /prod/patients/{id}             → Update patient record
DELETE /prod/patients/{id}           → Delete patient record
```

### Data Flow Examples

Clinical Notes Generation

```
1) User fills ClinicalNotes.jsx form
2) Frontend → POST /prod/generate-notes
3) API Gateway → ehr-clinical-notes Lambda
4) Lambda: validate → call Bedrock Titan → format SOAP
5) Response → { "soap_note": "SUBJECTIVE: ..." }
6) Frontend renders formatted note
```

ICD‑10 Coding

```
1) User enters clinical text in ICD10Coding.jsx
2) Frontend → POST /prod/suggest-icd10
3) Lambda validates → analyzes → suggests codes
4) Response → { "codes": [ {code, description, confidence}, ... ] }
5) Frontend displays table with confidence scores
```

---

## 🧱 Architecture

| Layer | Stack |
|-------|------|
| Frontend | React 18, Vite, MUI, Axios |
| Backend | FastAPI (local dev), AWS Lambda via API Gateway (prod) |
| AI / NLP | Amazon Bedrock (Titan Text), Azure OpenAI GPT‑4 Vision, BioBERT |
| Imaging | OpenCV pipeline + U‑Net |
| Data | DynamoDB (records), S3 (images/models) |
| IaC & Ops | CloudFormation, IAM, CloudWatch |
| Region | us-east-1 |

---

## 🛠 Technology Stack

- Frontend: React, Vite, MUI, Axios, React Router
- Backend: FastAPI, Boto3, AWS Lambda, API Gateway, DynamoDB
- AI/ML: Amazon Titan Text Express, Azure OpenAI GPT‑4/Vision, U‑Net, BioBERT/BioGPT
- Tooling: PyTest, Coverage, Jupyter, Black, Flake8
- Infra: CloudFormation, IAM, S3, CloudWatch

---

## 🚀 Quick Start

Prerequisites:
- Python 3.11+, Node.js 16+, AWS CLI configured
- Optional: Azure OpenAI credentials

Clone & setup:
```bash
git clone https://github.com/23f2003700/Infosys-intern-2025.git
cd Infosys-intern-2025
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
```

Run backend locally:
```bash
python start_server.py
# http://localhost:8000/docs (local FastAPI swagger)
```

Run demo:
```bash
python examples/demo.py
```

Frontend build & deploy (S3):
```bash
cd frontend
npm install
echo "VITE_API_URL=https://cvu4o3ywpl.execute-api.us-east-1.amazonaws.com/prod" > .env.production
npm run build
aws s3 sync dist/ s3://ehr-frontend-48208/ --delete
# App: http://ehr-frontend-48208.s3-website-us-east-1.amazonaws.com
```

Infrastructure (CloudFormation):
```bash
cd infrastructure
aws cloudformation create-stack \
  --stack-name ehr-ai-stack \
  --template-body file://cloudformation-template.yaml \
  --capabilities CAPABILITY_IAM \
  --region us-east-1
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /prod/ | Root (returns Missing Authentication Token) |
| POST | /prod/generate-notes | Generate clinical SOAP/progress/discharge notes |
| POST | /prod/suggest-icd10 | Suggest ICD‑10 codes |
| POST | /prod/enhance-image | Enhance medical images |
| POST | /prod/patients | Create patient record |
| GET | /prod/patients/{id} | Read patient record |
| PUT | /prod/patients/{id} | Update patient record |
| DELETE | /prod/patients/{id} | Delete patient record |

Example usage:
```python
import requests

API = "https://cvu4o3ywpl.execute-api.us-east-1.amazonaws.com/prod"

requests.post(f"{API}/enhance-image",
              json={"image_base64": "<base64>", "modality": "xray"})

requests.post(f"{API}/generate-notes",
              json={"patient_info": {"name":"John Doe","age":45},
                    "findings": "Patient presents with chest pain..."})

requests.post(f"{API}/suggest-icd10",
              json={"clinical_text": "Patient with hypertension and diabetes", "top_k": 3})
```

---

## 🔧 Configuration

Environment variables:

```bash
# Azure OpenAI (optional, for GenAI features)
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4
AZURE_OPENAI_VISION_DEPLOYMENT=gpt-4-vision

# Backend
BEDROCK_MODEL_ID=amazon.titan-text-express-v1
DYNAMODB_TABLE_NAME=ehr-patient-records
AWS_REGION=us-east-1
SAGEMAKER_ENDPOINT=biogpt-medical-endpoint  # optional

# Local API (dev)
API_HOST=0.0.0.0
API_PORT=8000

# Frontend (.env.production)
VITE_API_URL=https://cvu4o3ywpl.execute-api.us-east-1.amazonaws.com/prod
```

Config file:
- Edit config/config.yaml for image parameters, model paths, API settings, and security options.

---

## 🔐 Security & Compliance

- IAM roles with least privilege
- Lambda execution roles bound to specific resources
- DynamoDB encryption at rest; S3 bucket policies
- API Gateway CORS enabled; throttling/rate limits
- Input validation (name length, age range, text length)
- Medical keyword detection (35+ terms); gibberish rejection
- HIPAA-aligned anonymization workflow

---

## 📈 Performance Metrics

Imaging
- PSNR improvement: 15–35 dB
- SSIM: 0.75–0.90
- Processing: ~0.9 s/image (CPU), ~0.35 s/image (GPU)

NLP / ICD‑10
- F1‑Score: 0.85–0.95
- Precision: 0.85–0.92
- Recall: 0.82–0.90
- Inference: ~100 ms/note

API
- Image enhancement: < 1 s
- Note generation: 2–5 s
- ICD‑10 suggestions: < 500 ms

---

## 📊 Cost Structure

Free tier utilization:
- Lambda: 1M requests/month
- API Gateway: 1M calls/month
- DynamoDB: 25 GB storage
- S3: 5 GB storage
- Bedrock Titan: Refer to current free-tier terms

Estimates beyond free tier:
- Lambda: ~$0.20 per 1M requests
- API Gateway: ~$3.50 per 1M requests
- DynamoDB: ~$0.25 per GB-month
- S3: ~$0.023 per GB-month

Current usage: Typically within free tier ($0–$5/mo depending on traffic)

---

## 🧪 Training & Notebooks

- 01_image_enhancement_training.ipynb
  - Train U‑Net, evaluate PSNR/SSIM, checkpointing (≈15–30 min CPU)
- 02_clinical_nlp_training.ipynb
  - Fine‑tune BioBERT for ICD‑10 (≈20–40 min CPU)
- 03_system_testing.ipynb
  - End‑to‑end system validation and benchmarking (≈5–10 min)

---

## ✅ Testing

Run all tests:
```bash
pytest tests/
```

Run specific module:
```bash
pytest tests/test_module1.py
pytest tests/test_module2.py
```

With coverage:
```bash
pytest --cov=src tests/
```

---

## 🛠 Deployment Workflow

Frontend (S3):
```bash
cd frontend
npm install
npm run build
aws s3 sync dist/ s3://ehr-frontend-48208/ --delete
# Result: http://ehr-frontend-48208.s3-website-us-east-1.amazonaws.com
```

Backend (Lambda):
```bash
cd backend/lambda_functions
zip -r lambda-package.zip *.py
aws s3 cp lambda-package.zip s3://ehr-deployment-340663646697/

aws lambda update-function-code \
  --function-name ehr-clinical-notes \
  --s3-bucket ehr-deployment-340663646697 \
  --s3-key lambda-package.zip \
  --region us-east-1
```

Infrastructure (CloudFormation):
```bash
cd infrastructure
aws cloudformation create-stack \
  --stack-name ehr-ai-stack \
  --template-body file://cloudformation-template.yaml \
  --capabilities CAPABILITY_IAM \
  --region us-east-1
```

---

## 🧪 API Testing (cURL)

Clinical Notes:
```bash
curl -X POST https://cvu4o3ywpl.execute-api.us-east-1.amazonaws.com/prod/generate-notes \
  -H "Content-Type: application/json" \
  -d '{"patient_info":{"name":"Test Patient","age":30},"findings":"Patient with chest pain and fever"}'
```

ICD‑10:
```bash
curl -X POST https://cvu4o3ywpl.execute-api.us-east-1.amazonaws.com/prod/suggest-icd10 \
  -H "Content-Type: application/json" \
  -d '{"clinical_text":"Patient with hypertension and diabetes"}'
```

Root (expected behavior):
```bash
curl https://cvu4o3ywpl.execute-api.us-east-1.amazonaws.com/prod
# {"message":"Missing Authentication Token"}
```

---

## 🧰 Troubleshooting

- "Missing Authentication Token" on /prod
  - Normal; use specific endpoints (e.g., /generate-notes)
- CORS errors
  - Ensure API Gateway CORS is enabled and responses include Access-Control-Allow-Origin: *
- Lambda timeout
  - Increase timeout; review CloudWatch logs; reduce prompt/model latency
- Bedrock access denied
  - Grant bedrock:InvokeModel in Lambda role; verify region/model ID
- DynamoDB throttling
  - Enable auto-scaling; increase RCU/WCU; implement exponential backoff

---

## 🔮 Future Enhancements

- CloudFront + HTTPS
- HL7/FHIR integration layer
- Multi-language support
- Predictive analytics and risk scoring
- Imaging anomaly detection
- Voice-to-text dictation
- Advanced analytics dashboard
- Mobile app (React Native)
- Appointment scheduling automation

---

## 📦 Module 2 Deliverables (Completed)

Location: data/output/module2_deliverables/
- Original and enhanced images
- Stepwise enhancement visualizations
- metrics_summary.json
- enhancement_summary_report.md

---

## 👩‍💻 Development

```bash
pip install -r requirements.txt
pip install pytest pytest-cov jupyter black flake8

black src/
flake8 src/
pytest --cov=src tests/
```

Key files:
- frontend/.env.production — API endpoint
- frontend/src/pages/*.jsx — UI pages
- frontend/src/services/api.js — API client
- backend/lambda_functions/*.py — Lambda handlers
- infrastructure/cloudformation-template.yaml — AWS resources
- config/config.yaml — Tunables and security options

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: git checkout -b feature/amazing-feature
3. Commit: git commit -m "Add amazing feature"
4. Push: git push origin feature/amazing-feature
5. Open a Pull Request

---

## 🏆 Project Status

| Module | Status |
|--------|--------|
| Module 1 – Preprocessing | ✅ Complete |
| Module 2 – Imaging Enhancement | ✅ Complete |
| Module 3 – Documentation & ICD‑10 | ✅ Complete |
| Module 4 – Integration & Deployment | ✅ Complete |
| Training Infrastructure | ✅ Complete |
| Testing Suite | ✅ Complete |
| Overall | 🎉 100% |

---

## 🙏 Acknowledgments

- Infosys Springboard Internship Program 2025
- Azure OpenAI & Amazon Bedrock teams
- PyTorch & FastAPI communities
- OpenCV and medical imaging OSS contributors

---

## 📞 Contact

Aaryan Choudhary  
Email: rampyaaryan17@gmail.com  
GitHub: [@23f2003700](https://github.com/23f2003700)  
Program: Infosys Springboard — Intern 2025

---

## 📝 License

Developed as part of the Infosys Springboard Internship Program 2025.  
See the LICENSE file for details.

---

Last Updated: 2025-11-12 • Version: 1.0.0
