from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    number: int


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Project S.A.B.I.N.E"}


@app.post("/item/")
async def create_item(item: Item):
    item.number += 28
    if (item.name == "tijtgat"):
        return {
            "message": "Erik stinkt"

        }
    return {
        "message": "Item aangemaakt",
        "item": item
    }
