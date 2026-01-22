from fastapi import FastAPI

from app.db.session import engine
from app.db.base import Base
from app.api.jobs import router as jobs_router
from app.api.match import router as match_router

app = FastAPI(
    title="Resume Matcher API",
    description="Scores resumes against job descriptions and tracks job applications",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(jobs_router)
app.include_router(match_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
