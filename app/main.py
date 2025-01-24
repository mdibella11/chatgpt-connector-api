
import os
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Get OpenAI API Key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY environment variable.")
openai.api_key = OPENAI_API_KEY

# Example API keys for authentication
VALID_API_KEYS = os.getenv("VALID_API_KEYS", "").split(",")

class ChatRequest(BaseModel):
    message: str

@app.get("/health")
async def health():
    return {"status": "API is running", "author": "Marco Di Bella"}

@app.post("/chat")
async def chat(request: ChatRequest, x_api_key: str = Header(None)):
    if x_api_key not in VALID_API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.message}]
        )
        answer = response.choices[0].message["content"].strip()
        return {"author": "Marco Di Bella", "message": request.message, "response": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
