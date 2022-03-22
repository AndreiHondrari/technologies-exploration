from fastapi import FastAPI


app = FastAPI()


@app.get('/some/')
async def index(this: int = 0, that: int = 0) -> str:
    return f"KEK_{this}_{that}"
