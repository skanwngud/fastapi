import uvicorn

from fastapi import FastAPI, Query
from typing import Optional, List


app = FastAPI()

@app.get("/models")
async def get_models(q: Optional[str] = Query(..., min_length=3, max_length=50,
                                              title="query class",
                                              description="this is query class",
                                              alias="query-alias"), l: Optional[List[str]] = Query(None,
                                                                                                   deprecated=True)):
    results = {"models": [{"model_name": "yolov8"}, {"model_name": "vedadet"}, {"q": q}]}
    if l:
        results.update({"l": l})
    return results


if __name__ == "__main__":
    uvicorn.run("query_class:app", reload=True)