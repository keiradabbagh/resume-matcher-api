from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.db.base import Base


class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    role = Column(String, nullable=False)
    status = Column(String, default="applied")
    applied_date = Column(DateTime, default=datetime.utcnow)
