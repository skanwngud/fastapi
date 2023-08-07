# Query Parameter
- 함수에 사용 되는 파라미터이나 `path parameter` 에는 없다.

# 예제
## 기본 예제
```python
# query_parameter.py

import uvicorn

from fastapi import FastAPI


app = FastAPI()

integer_list = range(100)

@app.get("/")
async def root(start: int, end:int=30):
    return {"values": list(integer_list[start: end])}


if __name__ == "__main__":
    uvicorn.run("query_parameter:app", host="127.0.0.1", port=8000, reload=True, reload_dirs="./", reload_excludes="README.md")
```
- 0 부터 99 까지 범위의 정수 리스트를 만들고 해당 리스트의 시작과 끝을 지정하여 슬라이싱한 결과를 리턴한다.
- 위 코드에서 파라미터로 받는 것은 `start` 와 `end` 인데, 보다시피 `path` 에는 아무런 인자가 들어오지 않는다.
- `http://127.0.0.1:8000/?start=0&end=10` 과 같은 형식으로 사용한다.
    - `?` 로 시작, 각 인자를 추가할 때마다 `&` 를 사용한다.
- `path parameter` 와 마찬가지로 타입을 받을 땐 전부 `str` 이지만 타입을 따로 명시해주면 형변환 된다.
- `default value` 도 추가 가능하다.

## Optional
```python
# qeury_parameter.py

import uvicorn

from typing import Optional
from fastapi import FastAPI


app = FastAPI()

integer_list = range(100)

@app.get("/")
async def get_root(start: Optional[int]=None, end: int=30):
    if start is None:
        return {"values": "the value got None."}

    return {"values": list(integer_list[start: end])}


if __name__ == "__main__":
    uvicorn.run("query_parameter:app", host="127.0.0.1", port=8000, reload=True, reload_dirs="./", reload_excludes="README.md")
```
- 타입을 `Optional` 로도 지정할 수 있으며, 따라서 `None` 값도 전달할 수 있다.

## 2개 이상의 path parameter 와 query parameter 사용
```python
# query_parameter.py

import uvicorn

from enum import Enum
from typing import Optional
from fastapi import FastAPI


app = FastAPI()

integer_list = range(100)

class ModelName(str, Enum):
    yolo = "yolo"
    efficient = "efficient"

class ModelVersion(str, Enum):
    v4 = "4"
    v8 = "8"

@app.get("/models/{name}/{version}")
async def get_root(name:ModelName, vresion: ModelVersion, start: Optional[int]=None, end: int=30):
    if start is None:
        start = end - 5 if end - 5 >= 0 else 0

    return {"model": {"name": name, "version": version}}, {"values": list(integer_list[start:end])}


if __name__ == "__main__":
    uvicorn.run("query_parameter:app", host="127.0.0.1", port=8000, reload=True, reload_dirs="./", reload_excludes="README.md")
```
- 두 개 이상의 `path`, `qeury parameter` 를 사용했으며 각각 사용자 정의 타입과 `Optional` 타입도 지정해줬다.

# Reference
- [fastapi 공식문서](https://fastapi.tiangolo.com/ko/)
- [붕어사랑 티스토리](https://lucky516.tistroy.com/category/Fast%20API)