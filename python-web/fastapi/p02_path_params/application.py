from fastapi import FastAPI


app = FastAPI()


@app.get('/some/{kek}')
async def index(kek: int) -> str:
    return f"KEK_{kek}"
