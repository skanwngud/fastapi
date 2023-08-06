import uvicorn

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    
@app.post("/items/")
async def request_item(item: Item):
    return item

@app.post("/items/{item_id}")
async def request_complex_item(item_id: int, item: Item, q: Optional[bool] = None):
    result = {"item_id": item_id, "item": {**item.dict()}}
    if q is not None:
        result.update({"q": q})
        
    return result


if __name__ == "__main__":
    uvicorn.run("request:app", host="127.0.0.1", port=8000, reload=True, reload_excludes="README.md", reload_dirs="./")