from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Working"}

@app.post("/summary")
async def summary(transcript: str):
    return {"summary": ["Good meeting", "Goodbye"]}
