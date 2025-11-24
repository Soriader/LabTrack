from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base
from datetime import datetime

class Sample(Base):
    __tablename__ = "sample"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    type = Column(String, nullable=False)
    temperature = Column(Float, nullable=True)
    description = Column(String, nullable=True)