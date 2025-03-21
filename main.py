from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, welcome to the greeting API!"}

@app.get("/japan")
def read_root():
    return {"message": "Konnichiwa"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT env var is not set
    uvicorn.run(app, host="0.0.0.0", port=port)
