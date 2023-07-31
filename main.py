import uvicorn

from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class ModelName(str, Enum):
    tinaface = "tinaface"
    yolov8 = "yolov8"
    dsfd = "dsfd"
    scrfd = "scrfd"

@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.get("/models/{model_name}")
async def model_selection(model_name: ModelName):
    if model_name == ModelName.tinaface:
        return {"model_name": model_name}
    
    elif model_name.value == "yolov8":
        return {"model_name": model_name}
    
    elif model_name == ModelName.dsfd:
        return {"model_name": "dsfd"}
    
    return {"model_name": "scrfd"}

if __name__ == "__main__":
    uvicorn.run(app=app, port=8080)