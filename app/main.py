from fastapi import FastAPI
from enum import Enum
from typing import Optional

## 有効なパスパラメータの値を定義したい場合  
## Enumを利用する
## リクエストパラメータの値は文字列型なので、intを継承したクラスを作成するとエラーになる
class ModelName(str, Enum):
    morning = 1
    noon = 2
    night = 3


fake_items_db = [{"item": "one"}, {"item": "two"}, {"item": "three"}]

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello:" : "World"}

@app.get("/greeting/{id}")
async def greet(id: ModelName):
    if id == ModelName.morning:
        greet = "GOOD MORNING"
    elif id == ModelName.noon:
        greet = "HELLO"
    elif id == ModelName.night:
        greet = "GOOD NIGHT"
    else:
        greet = "WRONG NUMBER"             
    return {"greeting": greet}

@app.get("/test")
async def test():
    return {"TEST": "MATH"}
  
## クエリパラメータ
@app.get("/items/")
async def itemQuery(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

## オプショナルパラメータ
## 下記形式だと
## raise fastapi.exceptions.FastAPIError(
## fastapi.exceptions.FastAPIError: Invalid args for response field! Hint: check that False is a valid pydantic field type

# @app.get("/optional")
# async def understandOptional(q: Optional[str] == None):
#     return q

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# bool型を宣言する