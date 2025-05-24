from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/picks")
def get_picks():
    try:
        with open("picks.json", "r") as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": str(e)}
