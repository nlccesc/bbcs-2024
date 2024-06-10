from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

@app.post("/")
def create_item(item: Item):
    return {"message": f"Hello from Service 1, {item.name}!", "description": item.description}

Instrumentator().instrument(app).expose(app)
