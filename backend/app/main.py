from fastapi import FastAPI
from app.db import SessionLocal

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}
