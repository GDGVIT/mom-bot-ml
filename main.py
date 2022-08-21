from fastapi import FastAPI
from src.summary import summarize

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Working"}

@app.post("/summary")
async def summary(transcript: str):
    return {"summary": summarize(transcript)}
