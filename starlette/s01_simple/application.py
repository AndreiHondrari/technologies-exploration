from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.requests import Request


async def homepage(request: Request) -> JSONResponse:
    return JSONResponse({'name': "Gandalf"})


app = Starlette(
    debug=True,
    routes=[
        Route('/', homepage),
    ]
)
