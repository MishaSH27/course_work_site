from typing import Union

import uvicorn
from fastapi import FastAPI

from core.config import settings

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__  == "__main__":
    uvicorn.run(app, host=settings.run.host, port=settings.run.port, reload=True, log_level="info")
