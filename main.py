from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/")
def home():
    logging.info("Home endpoint called")
    return {"message": "API is running"}

@app.get("/hello/{name}")
def hello(name: str):
    logging.info(f"Hello called for {name}")
    return {"hello": name}