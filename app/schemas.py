from pydantic import BaseModel, Field


class EmailRequest(BaseModel):
    email: str = Field(
        ...,
        min_length=10,
        max_length=10000,
        description="Email text to analyze"
    )


class CategoryScore(BaseModel):
    score: int = Field(ge=0)
    max_score: int = Field(gt=0)
    feedback: str


class EmailAnalysisResponse(BaseModel):
    overall_score: int = Field(ge=0, le=100)

    clarity: CategoryScore
    professionalism: CategoryScore
    grammar: CategoryScore
    tone: CategoryScore
    structure: CategoryScore
    conciseness: CategoryScore

    summary: str
    strengths: list[str]
    improvements: list[str]
    improved_email: str