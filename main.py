from fastapi import FastAPI 

app = FastAPI()

# get, post, put, and delete

@app.get("/")
def welcome():
    return {"message": "Hello world"}