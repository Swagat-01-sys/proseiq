from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .schemas import EmailRequest, EmailAnalysisResponse
from .services.email_analyzer import EmailAnalyzer


load_dotenv()


app = FastAPI(
    title="ProseIQ API",
    description="AI-powered business communication analysis API",
    version="1.0.0"
)


# Temporary CORS setup for development.
# We can restrict this to the actual frontend domain later.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


analyzer = EmailAnalyzer()


@app.get("/")
async def root():
    return {
        "message": "ProseIQ API is running",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


@app.post(
    "/api/analyze",
    response_model=EmailAnalysisResponse
)
async def analyze_email(request: EmailRequest):

    try:
        result = analyzer.analyze(request.email)
        return result

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc)
        )

    except Exception as exc:
        print(f"Analysis error: {exc}")

        raise HTTPException(
            status_code=500,
            detail="Unable to analyze email."
        )