from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.sample_schema import SampleCreate, SampleRead
from app.models.sample_model import Sample

router = APIRouter(
    prefix="/samples",
    tags=["Samples"]
)

@router.get("/", response_model=list[SampleRead])
def get_samples(db: Session = Depends(get_db)):
    samples = db.query(Sample).all()
    return samples