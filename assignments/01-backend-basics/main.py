from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/echo")
async def echo(msg: Message):
    return {"echo": msg.message}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
