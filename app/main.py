#Import FastAPI framework
from fastapi import FastAPI

#create FastAPI app instance
app = FastAPI(
    title="Resume Matcher API",
    description="Scores resumes against job descriptions and tracks job applications",
    version="0.1.0"
)

#health check endpoint
@app.get("/health")
def health_check():
    # Return service status
    return {"status": "ok"}
