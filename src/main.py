from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "My API is working"
    }


@app.get("/discovery")
def discovery():
    return {
        "message": "This API provides tools for querying sales and marketing data."
    }
