from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI"} # returns a dictionary (fastAPI automatically converts it into JSON)