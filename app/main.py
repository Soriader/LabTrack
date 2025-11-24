from fastapi import FastAPI
from app.database import engine, Base
from app.models.sample_model import Sample

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "LabTrack API running"}