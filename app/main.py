<<<<<<< HEAD

=======
from fastapi import FastAPI

from app.db.session import engine
from app.db.base import Base
from app.api.jobs import router as jobs_router
from app.api.match import router as match_router

app = FastAPI(
    title="Resume Matcher API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(jobs_router)
app.include_router(match_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
>>>>>>> f9c1041 (Add resume-to-job matching with TF-IDF scoring)
