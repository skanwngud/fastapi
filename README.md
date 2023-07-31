# fastapi
FastAPI

## 설치
```shell
pip install fastapi
pip install "uvicorn[standard]"
```

## Hello World 출력
```python
import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hell World"}


if __name__ == "__main__":
    uvicorn.run(app=app, port=8080)
```
- ```uvicorn.run(app=app, port=8080)``` 은 터미널 상에서 ```uvicorn main:app --port=8080 --reload``` 와 동일하다.
- 해당 명령어들은 ```127.0.0.1:8080``` 에서 접속 가능하다.

## API docs
- ```127.0.0.1:8080/docs```, ```127.0.0.1:8080/redoc``` 으로 접속하면 ```swagger``` 를 기본 제공하는 것을 확인할 수 있다.
- 위 페이지는 코드상으로 구현한 백엔드를 테스트할 수 있다.

## Operation
- `FastAPI` 에서 `operation` 은 `HTTP` 의 `method` 를 의미한다.
    - `POST`: 서버에 데이터를 새로 생성한다.
    - `GET`: 서버에 존재하는 데이터를 받아온다.
    - `PUT`: 기존에 존재하는 서버의 데이터를 변경한다. (업데이트한다.)
    - `DELETE`: 서버의 데이터를 삭제한다.

## Path parameter
```python
@app.get("/models/{name}")
async def read_model(name):
    return {"model_name": name}
```
- 주소로부터 `parameter` 를 입력 받는다.

## Path Parameter 심화
- Path parameter 의 타입지정
- Predefined value 로 request check
- Path Operataion
```python
from enum import Enum

class ModelName(str, Enum):  # 열거형 enum 을 통해 모델 이름 명시.
    tinaface = "tinaface"
    yolov8 = "yolov8"
    dsfd = "dsfd"
    scrfd = "scrfd"

@app.get("/models/me")  # operation 의 순서문제로 models/me 가 먼저 나올 수 있음.
async def model_me():
    return {"model_name": "me"}

@app.get("/models/{model_name}")  # 모델 이름을 입력 받는다.
async def model_selection(model_name: ModelName):  # model_name 의 타입을 지정한다.
    if model_name == ModelName.tinaface:  # 각 조건에 맞는 모델 이름 출력.
        return {"model_name": model_name}
    
    elif model_name.value == "yolov8":
        return {"model_name": model_name}
    
    elif model_name == ModelName.dsfd:
        return {"model_name": "dsfd"}
    
    return {"model_name": "scrfd"}
```
# Reference
[FastAPI official documents](https://fastapi.tiangolo.com/ko/)  
[붕어사랑 티스토리](https://lucky516.tistory.com/category/Fast%20API)