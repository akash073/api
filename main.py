from fastapi import FastAPI
import logging

from pydantic import BaseModel
from typing import Optional

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

class LocationData(BaseModel):
    ip: Optional[str] = None
    hostname: Optional[str] = None
    city: Optional[str] = None
    region: Optional[str] = None
    country: Optional[str] = None
    loc: Optional[str] = None
    org: Optional[str] = None
    postal: Optional[str] = None
    timezone: Optional[str] = None

@app.post("/location")
async def receive_location(data: LocationData):
    logging.info(f"Received location: {data}")
    # Save to DB, log it, etc.
    return {"status": "success", "received": data}