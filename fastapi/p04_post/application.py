import dataclasses as dc

from typing import Dict
from fastapi import FastAPI


@dc.dataclass
class Some:
    x: int
    y: int
    descr: str


app = FastAPI()


@app.get('/')
async def index() -> Dict[str, str]:
    return {'hey': 'you'}


@app.post('/potato')
async def potato(something: Some) -> str:
    return f"GOT _ {something}"
