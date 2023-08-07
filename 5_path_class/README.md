# Path Class
- `path parameter` 를 좀 더 다양한 기능을 통해 사용할 수 있는 클래스.

# 예제
## 기본 예제
```python
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
```
- `query class` 와 마찬가지로 `title` 을 지정할 수 있다.
- 숫자를 제한할 수 있다.
    - `ge`: greater than or equal, 크거나 같다
    - `gt`: greater than, 크다
    - `lt`: less than, 작다
    - `le`: less than or equal, 작거나 같다

# Reference
- [fastapi 공식문서](https://fastapi.tiangolo.com/ko/)
- [붕어사랑 티스토리](https://lucky516.tistroy.com/category/Fast%20API)