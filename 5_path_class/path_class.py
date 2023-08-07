import uvicorn

from fastapi import FastAPI, Path


app = FastAPI()

@app.get("/models/{model_name}")
async def get_models(model_name: str = Path(...,
                                        title="this is path class",
                                        ge=1)):
    return {"message": model_name}


if __name__ == "__main__":
    uvicorn.run("path_class:app")