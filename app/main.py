
import os
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from dotenv import load_dotenv
import openai

load_dotenv()

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set in the environment variables.")

openai.api_key = OPENAI_API_KEY

VALID_API_KEYS = os.getenv("VALID_API_KEYS", "").split(",")

class ChatRequest(BaseModel):
    message: str

@app.get("/health")
async def health():
    return {"status": "API is running", "author": "Marco Di Bella"}

@app.post("/chat")
async def chat_with_gpt(request: ChatRequest, x_api_key: str = Header(None)):
    if x_api_key not in VALID_API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.message}]
        )
        reply = response['choices'][0]['message']['content'].strip()
        return {"author": "Marco Di Bella", "reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
