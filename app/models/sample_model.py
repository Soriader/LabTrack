from sqlalchemy import Column, Integer, String, DateTime, Float
from app.database import Base
import datetime

class Sample(Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    type = Column(String(50), nullable=False)
    temperature = Column(Float, nullable=True)
    description = Column(String(255), nullable=True)