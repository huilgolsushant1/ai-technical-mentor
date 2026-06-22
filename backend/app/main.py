from fastapi import FastAPI

from app.api.assessment import router as assessment_router
app = FastAPI(
    title="AI Technical Mentor API",
    description="Backend API for AI Technical Mentor",
    version="0.1.0"
)

app.include_router(assessment_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to AI Technical Mentor API"
    }