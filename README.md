# ProseIQ

### AI-Powered Communication Intelligence

ProseIQ is an AI-powered communication analysis platform that evaluates written emails across key communication dimensions and provides actionable feedback to help users write more clearly, professionally, and effectively.

---

## Live Backend

**Backend API:**  
https://proseiq-backend.onrender.com

**Interactive API Documentation:**  
https://proseiq-backend.onrender.com/docs

**Health Check:**  
https://proseiq-backend.onrender.com/healths

**live app Url**
https://email-analyser-lyart.vercel.app/

## Overview

ProseIQ analyzes an email and generates a communication score based on six core dimensions:

| Dimension       |  Weight |
| --------------- | ------: |
| Clarity         |      20 |
| Professionalism |      20 |
| Grammar         |      15 |
| Tone            |      15 |
| Structure       |      15 |
| Conciseness     |      15 |
| **Total**       | **100** |

In addition to the overall score, ProseIQ provides:

* Detailed category-level feedback
* Key strengths
* Areas for improvement
* AI-improved version of the email

---

## Current Architecture

```text
User
  │
  ▼
Frontend
  │
  │ POST /api/analyze
  ▼
FastAPI Backend
  │
  ▼
Gemini API
  │
  ▼
Structured Analysis
  │
  ▼
JSON Response
  │
  ▼
Frontend Results
```

---

## Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn
* Pydantic
* Python-dotenv

### AI

* Google Gemini API
* `google-genai`

### Development

* Git
* GitHub
* REST API
* Swagger / OpenAPI

### Frontend

Frontend integration is being developed separately and will consume the FastAPI REST API.

---

## Project Structure

```text
proseIQ/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── schemas.py
│   │   │
│   │   ├── prompts/
│   │   │   ├── __init__.py
│   │   │   └── email_prompt.py
│   │   │
│   │   └── services/
│   │       ├── __init__.py
│   │       └── email_analyzer.py
│   │
│   ├── requirements.txt
│   ├── .env
│   └── .gitignore
│
└── frontend/
```

---

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

### Analyze Email

```http
POST /api/analyze
```

Request:

```json
{
  "email": "Dear Sir, I am writing to ask about the status of my interview. Please let me know if there is any update. Thank you."
}
```

Response:

```json
{
  "overall_score": 72,
  "clarity": {
    "score": 13,
    "max_score": 20,
    "feedback": "The request is understandable, but key context is omitted."
  },
  "professionalism": {
    "score": 12,
    "max_score": 20,
    "feedback": "The email can be made more modern and professional."
  },
  "grammar": {
    "score": 14,
    "max_score": 15,
    "feedback": "The grammar is mostly correct."
  },
  "tone": {
    "score": 11,
    "max_score": 15,
    "feedback": "The tone is polite but somewhat abrupt."
  },
  "structure": {
    "score": 8,
    "max_score": 15,
    "feedback": "The email would benefit from standard formatting."
  },
  "conciseness": {
    "score": 14,
    "max_score": 15,
    "feedback": "The message is concise and direct."
  },
  "summary": "The email communicates its purpose clearly but needs improvements in structure, context, and professional tone.",
  "strengths": [
    "Clear purpose",
    "Polite wording",
    "Concise communication"
  ],
  "improvements": [
    "Add relevant context",
    "Improve email structure",
    "Use a more professional greeting"
  ],
  "improved_email": "Dear Hiring Manager,..."
}
```

---

## Backend Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/proseiq.git
cd proseiq
```

### 2. Move into the backend

```bash
cd backend
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file inside the `backend` directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

### Important

Never commit `.env` or expose your Gemini API key publicly.

The `.gitignore` file should include:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

## Running the Backend

From the `backend` directory:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### Interactive API Documentation

FastAPI automatically provides Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Open the documentation to test API endpoints directly from your browser.

---

## Development Workflow

ProseIQ is being developed collaboratively using Git and GitHub.

### Branches

```text
main
│
├── feature/backend
└── feature/frontend
```

### Example commit convention

```text
feat: add email analysis schema
feat: integrate Gemini analyzer
feat: add email analysis endpoint
fix: improve API error handling
docs: update project README
```

---

## Roadmap

### Phase 1 — Backend

* [x] FastAPI application
* [x] Health endpoint
* [x] Email analysis endpoint
* [x] Gemini integration
* [x] Structured AI response
* [x] Input validation
* [x] API documentation

### Phase 2 — Frontend

* [ ] Email editor
* [ ] Overall communication score
* [ ] Category score cards
* [ ] Strengths and improvements
* [ ] Improved email view
* [ ] Responsive UI

### Phase 3 — Deployment

* [ ] Deploy FastAPI backend
* [ ] Deploy frontend
* [ ] Configure production CORS
* [ ] Connect frontend and backend
* [ ] End-to-end testing

---

## Future Enhancements

Potential future improvements include:

* Email tone presets
* Formality adjustment
* Subject-line analysis
* Different writing contexts such as job applications, academic emails, and business communication
* User history and analytics
* Multi-language support
* Personalized writing recommendations

---

## Contributors

**ProseIQ Team**

* Backend Development — FastAPI, Gemini API, API architecture
* Frontend Development — User interface and frontend integration

---

## License

This project is currently intended for educational and portfolio purposes.

---

## Project Status

**Current Status:** Backend MVP completed and tested locally.

The FastAPI backend successfully accepts an email, analyzes it using Gemini, and returns a structured communication assessment through the REST API.