# 설치
```shell
pip install fastapi
pip install "uvicorn[standard]"
```

# 기본 예제
## 서버 실행
```python
#init.py

import uvicorn

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello world!"}


if __name__ == "__main__":
    uvicorn.run("init:app", host="127.0.0.1", port=8000, reload=True, reload_dirs="./", reload_excludes="./README.md")
```
- 위 코드 실행 후 [http://127.0.0.1:8000](http://127.0.0.1:8000) 로 접속하면 `{"message": "hello world"}` 라는 메세지를 볼 수 있다.

## API docs wjqthr
- API docs 란 사용자가 정의한 `api` 를 테스트 할 수 있는 페이지를 의미한다.
- 해당 페이지에서 `request` 등을 테스트해볼 수 있다.
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

# operation (method)
- `POST`: 데이터를 생성 (`CREATE`)
- `GET`: 생성 된 데이터를 불러옴 (`READ`)
- `PUT`: 생성 된 데이터를 수정 (`UPDATE`)
- `DELETE`: 데이터를 삭제 (`DELETE`)

# Reference
- [fastapi 공식문서](https://fastapi.tiangolo.com/ko/)
- [붕어사랑 티스토리](https://lucky516.tistroy.com/category/Fast%20API)