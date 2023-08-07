# Query Class
- `query parameter` 를 좀 더 다양한 기능을 통해 사용할 수 있도록 만들어주는 클래스.
- `from fastapi import Query` 의 형태로 `import` 한다.

# 예제
## 기본 예제
```python
# query_class.py

import uvicorn

from fastapi import FastAPI, Query
from typing import Optional


app = FastAPI()

@app.get("/models")
async def get_models(q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):
    results = {"models": [{"model_name": "yolov8"}, {"model_name": "vedadet"}]}
    if q:
        results.update({"q": q})
    
    return results


if __name__ == "__main__":
    uvicorn.run("query_class:app", reload=True)
```
- 파라미터의 최소, 최대 길이를 지정할 수 있으며 정규식으로 파라미터의 내용을 제한할 수도 있다.
- `default value` 도 작성할 수 있으며 이 경우엔 가장 앞에 들어온다.
    - `None` 이 들어왔기 때문에 타입이 `Optional` 이 된다.

## 파라미터를 필수 (required) 로 지정하고 list value 사용
```python
# query_class.py

import uvicorn

from fastapi import FastAPI, Query
from typing import Optional, List


app = FastAPI()

@app.get("/models")
async def get_models(q: Optional[str] = Query(..., min_length=3, max_length=50), l: Optional[List[str]] = Query(None)):
    results = {"models": [{"model_name": "yolov8"}, {"model_name": "vedadet"}, {"q": q}]}
    if l:
        results.update({"l": l})
    return results


if __name__ == "__main__":
    uvicorn.run("query_class:app", reload=True)
```
- `...` 를 사용하면 파라미터를 필수로 전달해야한다.
- 리스트 형태의 파라미터는 `127.0.0.1/models?l=hello&l=world` 와 같은 식으로 작성한다.

## Meta data
```python
# query_class.py

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
```
- `title`, `description` 등으로 파라미터에 대한 메타 데이터를 지정한다.
- 'query-alias' 처럼 일반적으로 파이썬에서 사용할 수 없는 형태의 문자열을 사용하고 싶다면 `alias` 를 사용한다.
    - `alias` 를 사용하면 `q` 처럼 원래의 변수명으로는 사용할 수 없다.
- `deprecated` 옵션을 통해 해당 파라미터가 더 이상의 유지보수 등을 시행하지 않는다는 것을 명시해준다.

# Reference
- [fastapi 공식문서](https://fastapi.tiangolo.com/ko/)
- [붕어사랑 티스토리](https://lucky516.tistroy.com/category/Fast%20API)