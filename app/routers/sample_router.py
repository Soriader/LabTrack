from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.sample_schema import SampleCreate, SampleRead
from app.models.sample_model import Sample

router = APIRouter(
    prefix="/samples",
    tags=["Samples"]
)

# READ ALL
@router.get("/", response_model=list[SampleRead])
def get_samples(db: Session = Depends(get_db)):
    samples = db.query(Sample).all()
    return samples

# READ ONE
@router.get("/{sample_id}", response_model=SampleRead)
def get_sample(sample_id: int, db: Session = Depends(get_db)):
    sample = db.query(Sample).filter(Sample.id == sample_id).first()

    if sample is None:
        raise HTTPException(status_code=404, detail="Sample not found")

    return sample

# CREATE
@router.post("/", response_model=SampleRead, status_code=201)
def create_sample(sample_data: SampleCreate, db: Session = Depends(get_db)):
    new_sample = Sample(
        name=sample_data.name,
        type=sample_data.type,
        temperature=sample_data.temperature,
        description=sample_data.description
    )

    db.add(new_sample)
    db.commit()
    db.refresh(new_sample)

    return new_sample

# UPDATE
@router.put("/{sample_id}", response_model=SampleRead)
def update_sample(sample_id: int, updated_data: SampleCreate, db: Session = Depends(get_db)):
    sample = db.query(Sample).filter_by(id=sample_id).first()

    if sample is None:
        raise HTTPException(status_code=404, detail="Sample not found")

    sample.name = updated_data.name
    sample.type = updated_data.type
    sample.temperature = updated_data.temperature
    sample.description = updated_data.description

    db.commit()
    db.refresh(sample)

    return sample

# DELETE
@router.delete("/{sample_id}", status_code=204)
def delete_sample(sample_id: int, db: Session = Depends(get_db)):
    sample = db.query(Sample).filter_by(id=sample_id).first()

    if sample is None:
        raise HTTPException(status_code=404, detail="Sample not found")

    db.delete(sample)
    db.commit()

    return None