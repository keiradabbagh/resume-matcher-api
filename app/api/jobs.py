from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.db.models import JobApplication
from app.schemas.job import JobCreate, JobRead

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.post("/", response_model=JobRead)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    new_job = JobApplication(**job.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job


@router.get("/", response_model=list[JobRead])
def list_jobs(db: Session = Depends(get_db)):
    return db.query(JobApplication).all()


@router.put("/{job_id}", response_model=JobRead)
def update_job(job_id: int, job: JobCreate, db: Session = Depends(get_db)):
    db_job = db.query(JobApplication).filter(JobApplication.id == job_id).first()

    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")

    for key, value in job.dict().items():
        setattr(db_job, key, value)

    db.commit()
    db.refresh(db_job)
    return db_job


@router.delete("/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(JobApplication).filter(JobApplication.id == job_id).first()

    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")

    db.delete(db_job)
    db.commit()
    return {"message": "Job deleted"}
