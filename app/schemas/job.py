from pydantic import BaseModel
from datetime import datetime


class JobBase(BaseModel):
    company: str
    role: str
    status: str = "applied"


class JobCreate(JobBase):
    pass


class JobRead(JobBase):
    id: int
    applied_date: datetime

    class Config:
        orm_mode = True
