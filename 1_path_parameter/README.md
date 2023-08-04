# Path Parameter
- 경로로부터 전달받는 파라미터를 의미한다.

# 예제
## 기본 예제
```python
@app.get("/models/{name}")
async def get_models_name(name):
    return {"model_name": name}
```

## 타입 지정
```python
@app.get("/models/{name}")
async def get_modelsname(name: str):
    return {"model_name": name}
```
- 지정한 타입과 맞지 않는 데이터 타입이 들어오면 에러가 발생한다.
- `str`, `int` 처럼 기본 설정 된 타입 말고도 `사용자 정의 타입` 을 만들어 지정할 수 있다.
- `path parameter` 는 기본적으로 인자를 받을 때 `str` 타입으로 받지만 타입을 명시해준다면 해당 타입으로 형변환 된다.

## predefined value 로 리퀘스트 체크
```python
# path_parameter.py

import uvicorn

from enum import Enum
from fastapi import FastAPI


app = FastAPI()

class ModelName(str, Enum):
    yolov8s = "yolov8s"
    yolov8m = "yolov8m"
    yolov8l = "yolov8l"

@app.get("/models/{path}")
async def get_model_path(path: ModelName):
    if path == ModelName.yolov8s:
        return {"model_name": path}

    elif path.value == "yolov8m":
        return {"model_name": path}

    return {"model_name": path}


if __name__ == "__main__":
    uvicorn.run("path_parameter:app", host="127.0.0.1", port=8000, reload=True, reload_dirs="./", reload_excludes="README.md")
```
- `path parameter` 로 전달 받은 인자는 `path.value` 처럼 값을 확인할 수 있다.
- 열거형 (enum) 으로 지정 된 타입들도 클래스의 매개변수처럼 확인 가능.

## path operation 순서
```python
# path_parameter.py

import uvicorn

from enum import Enum
from fastapi import FastAPI


app = FastAPI()

class ModelName(str, Enum):
    yolov8s = "yolov8s"
    yolov8m = "yolov8m"
    yolov8l = "yolov8l"

@app.get("/models/{path}")
async def get_model_path(path: ModelName):
    if path == ModelName.yolov8s:
        return {"model_name": path}

    elif path.value == "yolov8m":
        return {"model_name": path}

    return {"model_name": path}

@app.get("models/me")
async def get_model_me():
    return {"model_name": "the model name is me"}


if __name__ == "__main__":
    uvicorn.run("path_parameter:app", host="127.0.0.1", port=8000, reload=True, realod_dris="./", reload_excludes="README.md")
```
- 함수를 작성할 때에는 항상 순서를 주의해야한다.
- operation 은 순서의 영향을 받는데, 위로 갈수록 우선순위가 높아진다.
- 위 코드의 경우 `"models/me"` 로 접속하게 되면 `ModelName` 의 `path` 에 `me` 라는 value 는 존재하지 않는다는 에러가 발생한다.
    - `"models/{path}"` 가 먼저 호출 되면서 `path` 에 `me` 를 추가하고 `ModelName` 에서 `me` 라는 키를 찾기 때문이다.