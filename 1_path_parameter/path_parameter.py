import uvicorn

from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    yolov8s = "yolov8s"
    yolov8m = "yolov8m"
    yolov8l = "yolov8l"
    
    
app = FastAPI()

@app.get("/models/{path}")
async def get_model_path(path: ModelName):
    if path == ModelName.yolov8s:
        return {"model_name": path}
    
    elif path.value == "yolov8m":
        return {"model_name": path}
    
    return {"model_name": path}

@app.et("/models/me")
async def get_model_me():
    return {"message": "get_moe_me"}


if __name__ == "__main__":
    uvicorn.run("path_parameter:app", host="127.0.0.1", port=8000, reload=True, reload_dirs="./", reload_excludes="README.md")