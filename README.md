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

A production-ready Electronic Health Record (EHR) AI platform that leverages **Generative AI**, **Medical Imaging Enhancement**, and **Automated Clinical Documentation** to streamline healthcare workflows. Built using **React**, **FastAPI**, **AWS Lambda**, **Amazon Bedrock**, **Azure OpenAI**, **DynamoDB**, and **deep learning models (U-Net, BioBERT)**.

**Author:** Aaryan Choudhary  
**Program:** Infosys Springboard Internship 2025  
**Email:** rampyaaryan17@gmail.com  

---

## 🔗 Live Resources

| Component | URL |
|----------|-----|
| Frontend (Static Site) | http://ehr-frontend-48208.s3-website-us-east-1.amazonaws.com |
| Public API (Prod) | https://cvu4o3ywpl.execute-api.us-east-1.amazonaws.com/prod |
| GitHub Repo | https://github.com/23f2003700/Infosys-intern-2025 |
| Issue Tracker | https://github.com/23f2003700/Infosys-intern-2025/issues |

---

## 📚 Table of Contents
1. [Key Features](#-key-features)
2. [Architecture](#-architecture)
3. [Project Structure](#-project-structure)
4. [Technology Stack](#-technology-stack)
5. [Quick Start](#-quick-start)
6. [Core Modules](#-modules)
7. [API Endpoints](#-api-endpoints)
8. [Configuration](#-configuration)
9. [Security](#-security--compliance)
10. [Performance Metrics](#-performance-metrics)
11. [Training & Notebooks](#-training--notebooks)
12. [Testing](#-testing)
13. [Troubleshooting](#-troubleshooting)
14. [Future Enhancements](#-future-enhancements)
15. [Contributing](#-contributing)
16. [Project Status](#-project-status)
17. [Acknowledgments](#-acknowledgments)
18. [Contact](#-contact)
19. [License](#-license)

---

## ✨ Key Features

### 🖼 Medical Imaging Enhancement
- Multi-modality support: X-ray, CT, MRI, Ultrasound, DXA
- Noise reduction (NLM), contrast optimization (CLAHE), sharpening, edge enhancement
- Deep Learning U-Net (31M params) with PSNR/SSIM evaluation
- Batch enhancement workflow & visual comparison artifacts

### 📝 Automated Clinical Documentation
- SOAP notes, progress notes, discharge summaries, radiology reports
- Intelligent medical terminology extraction
- Bedrock + Azure OpenAI hybrid generation strategy

### 🏷 ICD-10 Coding Assistant
- Multi-label classification with confidence scores
- Fine-tuned BioBERT / BioGPT compatible
- Suggests common diagnostic codes (I10, E11.9, J44.9, etc.)

### 👥 Patient Management
- Structured patient profile storage (DynamoDB)
- Visit histories, demographic validation
- Secure anonymization workflows

### 🔐 Security & Validation
- Input validation (35+ medical keywords)
- HIPAA-aligned anonymization procedures
- IAM least-privilege architecture, encrypted storage

### 🚀 Production-Ready
- RESTful FastAPI backend
- AWS Lambda & API Gateway integration
- React + MUI responsive frontend
- Comprehensive test suite & notebooks

---

## 🧭 Architecture

| Layer | Stack |
|-------|-------|
| Frontend | React 18, Vite, MUI, Axios |
| Backend | FastAPI on AWS Lambda via API Gateway |
| AI / NLP | Amazon Bedrock (Titan Text), Azure OpenAI GPT-4 Vision, BioBERT |
| Imaging | OpenCV + U-Net pipeline |
| Database | DynamoDB (patient records) + S3 (images/models) |
| Infrastructure | AWS CloudFormation, IAM, CloudWatch |
| Monitoring | Metrics + logs (CloudWatch), JSON artifacts |
| Region | us-east-1 |

---

## 📁 Project Structure

```
ehr-ai-system/
├── src/
│   ├── module1_data_preprocessing/
│   ├── module2_image_enhancement/
│   ├── module3_documentation_automation/
│   └── module4_integration/
├── notebooks/
│   ├── 01_image_enhancement_training.ipynb
│   ├── 02_clinical_nlp_training.ipynb
│   └── 03_system_testing.ipynb
├── models/
│   ├── image_enhancement/
│   └── icd10_coding/
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
├── tests/
├── examples/
├── config/
├── docs/
└── README.md
```

---

## 🛠 Technology Stack

### Frontend
- React, Vite, MUI, Axios, React Router

### Backend
- FastAPI, Boto3, AWS Lambda, API Gateway, DynamoDB

### AI / ML
- Amazon Titan Text Express
- Azure OpenAI GPT-4 & GPT-4 Vision
- U-Net (image enhancement)
- BioBERT / BioGPT (ICD-10 coding)

### Dev & Ops
- CloudFormation, IAM, S3, CloudWatch
- Testing: PyTest, Coverage, Integration scripts

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 16+
- AWS CLI configured
- (Optional) Azure OpenAI credentials

### Clone & Environment

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

### Run Backend (Local FastAPI)
```bash
python start_server.py
# Visit: http://localhost:8000/docs
```

### Run Demo Script
```bash
python examples/demo.py
```

### Frontend Build & Deploy
```bash
cd frontend
npm install
echo "VITE_API_BASE_URL=https://YOUR-API-ID.execute-api.us-east-1.amazonaws.com/prod" > .env.production
npm run build
aws s3 sync dist/ s3://YOUR-FRONTEND-BUCKET/ --delete
```

### Infrastructure (CloudFormation)
```bash
cd infrastructure
aws cloudformation create-stack \
  --stack-name ehr-ai-stack \
  --template-body file://cloudformation-template.yaml \
  --capabilities CAPABILITY_IAM \
  --region us-east-1
```

---

## 🧩 Modules

| Module | Focus | Highlights |
|--------|-------|-----------|
| 1 | Data Preprocessing | DICOM/NIfTI loading, normalization, anonymization |
| 2 | Image Enhancement | U-Net training, NLM/CLAHE pipeline, PSNR/SSIM |
| 3 | Documentation & ICD-10 | SOAP notes, discharge summaries, BioBERT classifier |
| 4 | Integration & API | Unified FastAPI services, batch orchestration |

---

## 🌐 API Endpoints (Representative)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| POST | /api/v1/enhance-image | Enhance medical image |
| POST | /api/v1/generate-note | Generate clinical note |
| POST | /api/v1/suggest-icd10 | ICD-10 code suggestion |
| POST | /api/v1/batch-process | Batch operations |

### Example Usage

```python
import requests

# Enhance image
requests.post(
    'http://localhost:8000/api/v1/enhance-image',
    json={'image_base64': '<base64>', 'modality': 'xray'}
)

# Generate SOAP note
requests.post(
    'http://localhost:8000/api/v1/generate-note',
    json={'patient_info': {...}, 'findings': [...], 'note_type': 'soap'}
)

# Suggest ICD-10 codes
requests.post(
    'http://localhost:8000/api/v1/suggest-icd10',
    json={'clinical_text': 'Patient with hypertension...', 'top_k': 3}
)
```

---

## 🔧 Configuration

### Environment Variables
```bash
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4
AZURE_OPENAI_VISION_DEPLOYMENT=gpt-4-vision

DB_HOST=localhost
DB_PORT=5432
DB_NAME=ehr_db
DB_USER=postgres
DB_PASSWORD=your_password

API_HOST=0.0.0.0
API_PORT=8000

BEDROCK_MODEL_ID=amazon.titan-text-express-v1
DYNAMODB_TABLE_NAME=ehr-patient-records
AWS_REGION=us-east-1
```

### Config File
Customize `config/config.yaml` for:
- Image enhancement parameters
- Model paths
- Security rules
- API tuning

---

## 🔐 Security & Compliance

- IAM roles with least privilege
- S3 + DynamoDB encryption at rest
- Input validation (age ranges, name formats)
- Medical keyword semantic guardrails
- API Gateway rate limiting (throttling)
- Option for anonymization pre-ingestion

---

## 📈 Performance Metrics

### Imaging
| Metric | Value |
|--------|-------|
| PSNR Improvement | 15–35 dB |
| SSIM | 0.75–0.90 |
| CPU Processing | ~0.9 s/image |
| GPU Processing | ~0.35 s/image |

### NLP / ICD-10
| Metric | Value |
|--------|-------|
| F1-Score | 0.85–0.95 |
| Precision | 0.85–0.92 |
| Recall | 0.82–0.90 |
| Inference Time | ~100 ms/note |

### API
| Endpoint | Latency |
|----------|---------|
| Image Enhancement | < 1 s |
| Note Generation | 2–5 s |
| ICD-10 Suggestion | < 500 ms |
| Health Check | < 100 ms |

---

## 🧪 Training & Notebooks

| Notebook | Purpose | Approx. Runtime |
|----------|---------|-----------------|
| 01_image_enhancement_training.ipynb | Train U-Net + PSNR/SSIM evaluation | 15–30 min (CPU) |
| 02_clinical_nlp_training.ipynb | Fine-tune BioBERT for ICD-10 | 20–40 min (CPU) |
| 03_system_testing.ipynb | End-to-end validation & benchmarking | 5–10 min |

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

## 🛠 Troubleshooting

| Issue | Possible Fix |
|-------|--------------|
| Lambda Timeout | Increase timeout in console / reduce model size |
| CORS Errors | Enable API Gateway CORS + correct headers |
| Bedrock Access Denied | Verify `bedrock:InvokeModel` IAM permissions |
| DynamoDB Throttling | Enable auto-scaling / increase RCU/WCU |
| Poor Enhancement Output | Check normalization + modality parameter |
| Invalid Input Rejection | Confirm medical keyword presence threshold |

---

## 🔮 Future Enhancements

- CloudFront + HTTPS distribution
- HL7/FHIR integration layer
- Multi-language clinical notes
- Predictive patient risk scoring
- Anomaly detection for imaging
- Voice-to-text dictation pipeline
- Advanced analytics dashboard
- Mobile app (React Native)
- Appointment scheduling automation

---

## 📊 Module 2 Deliverables (Completed)

Artifacts stored in: `data/output/module2_deliverables/`  
Includes:
- Original + enhanced images
- Stepwise enhancement visualizations
- `metrics_summary.json`
- `enhancement_summary_report.md`

---

## 🧪 Development Workflow

```bash
# Install dev tooling
pip install -r requirements.txt
pip install pytest pytest-cov black flake8 jupyter

# Format
black src/

# Lint
flake8 src/

# Test
pytest --cov=src tests/
```

---

## 🤝 Contributing

1. Fork the repository  
2. Create a branch: `git checkout -b feature/amazing-feature`  
3. Commit: `git commit -m "Add amazing feature"`  
4. Push: `git push origin feature/amazing-feature`  
5. Open a Pull Request  

---

## 🏆 Project Status

| Module | Status |
|--------|--------|
| Module 1 – Preprocessing | ✅ Complete |
| Module 2 – Imaging Enhancement | ✅ Complete |
| Module 3 – Documentation & ICD-10 | ✅ Complete |
| Module 4 – Integration & Deployment | ✅ Complete |
| Training Infrastructure | ✅ Complete |
| Testing Suite | ✅ Complete |
| Overall | 🎉 100% |

---

## 🙏 Acknowledgments

- Infosys Springboard Internship Program  
- Azure OpenAI & Amazon Bedrock teams  
- PyTorch & FastAPI communities  
- Open-source medical imaging contributors  
- OpenCV developers  

---

## 📞 Contact

**Aaryan Choudhary**  
📧 Email: rampyaaryan17@gmail.com  
🔗 GitHub: [@23f2003700](https://github.com/23f2003700)  
🏫 Program: Infosys Springboard - Intern 2025  

---

## 📝 License

This project is developed as part of the **Infosys Springboard Internship Program 2025**.  
Please review the `LICENSE` file in the repository for terms.

---

## ⭐ Support

If you find this project valuable, consider giving it a star on GitHub!  
Your feedback and collaboration requests are welcome.

---

> Last Updated: November 12, 2025 • Version: 1.0.0
