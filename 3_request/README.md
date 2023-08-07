# Request
- `request`; 클라이언트가 API 서버에 데이터를 보낼 때 사용 되는 데이터.
- `response`; API 서버가 클라이언트에게 받은 데이터를 통해 처리한 응답을 클라이언트에게 보내는 데이터.
- `path` 와 `qurey` 는 url 을 통해 주고 받는 데이터를 볼 수 있지만, `request`, `respone` 는 url 을 통해 확인할 수 없다.

# 예제
## 기본 예제
```python
# request.py

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


if __name__ == "__main__":
    uvicorn.run("request:app", host="127.0.0.1", port=8000, reload=True, reload_excludes="README.md", reload_dirs="./")
```
- `/items` 라는 주소로 `item` 이라는 데이터를 요청하는 코드이다.
- `127.0.0.1` 으로 들어가면 단순 요청페이지라 요청이 제대로 되는지 테스트를 하고 싶으면 `/docs` 로 들어가서 확인한다.
- `pydantic` 의 `BaseModel` 로 클래스를 만들어 요청 데이터의 모양을 지정해준다.
    - 타입은 `Optional` 도 가능하며 `default` 값도 전달할 수 있다.
    - 따라서 `None` 값을 기본값으로 하는 데이터 형태를 만들었다.

## Path, Query, Request 사용 예제
```python
# request.py

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
    result = {"item_id": item_id, **item.dict()}
    if q is not None:
        result.update({"q": q})
        
    return result


if __name__ == "__main__":
    uvicorn.run("request:app", host="127.0.0.1", port=8000, reload=True, reload_excludes="README.md", reload_dirs="./")
```
- `path parameter`, `query parameter`, `request data` 를 전부 사용한다.
- 파라미터가 `path` 에 정의 되어있는지 `query` 에 정의 되어있는지 아니면 **`BaseModel` 의 형태로 저장 되어있는지**에 따라 해석한다.

# Reference
- [fastapi 공식문서](https://fastapi.tiangolo.com/ko/)
- [붕어사랑 티스토리](https://lucky516.tistroy.com/category/Fast%20API)