from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Route
from starlette.templating import Jinja2Templates
from starlette.exceptions import HTTPException


templates = Jinja2Templates(directory='templates')


async def home(request: Request) -> Jinja2Templates.TemplateResponse:
    context = {'request': request}
    return templates.TemplateResponse('home.html', context)


async def not_found(
    request: Request,
    exc: HTTPException,
) -> Jinja2Templates.TemplateResponse:
    context = {'request': request}
    return templates.TemplateResponse('404.html', context)


ROUTES = [
    Route('/', home, name="home"),
]


EXCEPTION_HANDLERS = {
    404: not_found,
}

app = Starlette(
    debug=True,
    routes=ROUTES,
    exception_handlers=EXCEPTION_HANDLERS,
)
