from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the API
@app.get("/")
def read_root():
    return {"message": "Hello, welcome to the greeting API!"}

@app.get("/japan")
def read_root():
    return {"message": "Konnichiwa"}
