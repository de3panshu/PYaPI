from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def greetDefault():
    return {"message": "Hello, welcome to the greeting API!"}

@app.get("/japan")
def greetJapan():
    return {"message": "Konnichiwa"}

@app.get("/spanish")
def greetSpanish():
    return {"message": "Hola"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
