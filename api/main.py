from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.get("/{num_1}/{num_2}")
def multiply(num_1: int, num_2: int):
    return {"result": num_1 * num_2}



