from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SampleBase(BaseModel):
    name: str
    type: str
    temperature: float | None = None
    description: str | None = None

class SampleCreate(SampleBase):
    pass

class SampleRead(SampleBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True

class SampleUpdate(SampleBase):
    id: int

