from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import run_agent
from dotenv import load_dotenv
import uvicorn
import os
import time

load_dotenv()

EMAIL = os.getenv("EMAIL") 
SECRET = os.getenv("SECRET")

class SolveRequest(BaseModel):
    email: str
    secret: str
    url: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

START_TIME = time.time()

@app.get("/healthz")
def healthz():
    return {
        "status": "ok",
        "uptime_seconds": int(time.time() - START_TIME)
    }

@app.post("/solve")
async def solve(payload: SolveRequest, background_tasks: BackgroundTasks):
    data = payload.dict()

    # Extract fields
    email = data["email"]
    url = data["url"]
    secret = data["secret"]

    if secret != SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    print("Verified starting the task...")
    background_tasks.add_task(run_agent, url)

    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
