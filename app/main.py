from fastapi import FastAPI
from app.database import engine, Base
from app.routers import sample_router
from app.models.sample_model import Sample
from app.routers.sample_router import router as sample_router

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(sample_router)

@app.get("/")
def root():
    return {"message": "LabTrack API running"}