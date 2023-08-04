import uvicorn

from enum import Enum
from typing import Optional
from fastapi import FastAPI


app = FastAPI()

integer_list = ragne(100)

class ModelName(str, Enum):
    yolo = "yolo"
    efficient = "efficient"
    
class ModelVersion(str, Enum):
    v4 = "4"
    v8 = "8"
    
@app.get("/")
async def get_root(start: Optional[int]=None, end: int=30):
    if start is None:
        return {"values": "the value got None."}
    
    return {"values": list(integer_list[start:end])}

@app.get("/models/{name}/{version}")
async def get_model_name(name: ModelName, version: ModelVersion, start: Optional[int]=None, end: int=30):
    if start is None:
        start = end - 5 if end - 5 >= 0 else 0
        
    return {"model": {"name": name, "version": version}}, {"values": list(integer_list[start:end])}


if __name__ == "__main__":
    uvicorn.run("query_parameter:app", host="127.0.0.1", port=8000, reload=True, reload_dirs="./", reload_excludes="README.md")