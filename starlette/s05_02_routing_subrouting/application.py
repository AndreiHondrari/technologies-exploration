import string

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.routing import Route, Mount
from starlette.exceptions import HTTPException

STYLE = ("""
<style>
    body {
        margin: 50px;
        font-size: 25px;
        color: white;

        --cval: 30;
        background-color: rgb(var(--cval), var(--cval), var(--cval));
    }

    a {
        color: green;
    }

    .link1 {
        text-decoration: none;
        color: white;
    }
</style>
""")

HTML = ("""
<html>
    <head>{head}</head>
    <body>{body}</body>
</html>
""")

HEADER = ("""
<a href="/" class="link1">
    <h1>Hello !</h1>
</a>
<hr>
""")

INDEX_BODY = f"""
{HEADER}
<p>The wood is light because it is not heavy</p>
<a href="/some/this">Some THIS</a><br>
<a href="/some/that">Some THAT</a><br>
"""

INDEX_CONTENT_TEMPLATE = HTML.format(head=STYLE, body=INDEX_BODY)


async def index(request: Request) -> HTMLResponse:
    content_template = string.Template(INDEX_CONTENT_TEMPLATE)
    html_result = content_template.substitute()
    return HTMLResponse(html_result)


THIS_BODY = f"""
{HEADER}
<h2>SOME / THIS ...<h2>
"""
THIS_CONTENT = HTML.format(head=STYLE, body=THIS_BODY)


async def this(request: Request) -> HTMLResponse:
    return HTMLResponse(THIS_CONTENT)


THAT_BODY = f"""
{HEADER}
<h2>SOME / THAT ...<h2>
"""
THAT_CONTENT = HTML.format(head=STYLE, body=THAT_BODY)


async def that(request: Request) -> HTMLResponse:
    return HTMLResponse(THAT_CONTENT)


ROUTES = [
    Route('/', index),
    Mount('/some/', routes=[
        Route('/this', this),
        Route('/that', that),
    ]),
]


async def not_found(request: Request, exc: HTTPException) -> HTMLResponse:
    CONTENT_BODY = f"""
    {HEADER}
    <h1>404 NOT FOUND !!!</h1>
    """
    CONTENT = HTML.format(head=STYLE, body=CONTENT_BODY)

    return HTMLResponse(CONTENT, status_code=exc.status_code)


async def server_error(request: Request, exc: HTTPException) -> HTMLResponse:
    CONTENT_BODY = f"""
    {HEADER}
    <h1>500 SERVER ERROR (ups....) !!!</h1>
    """
    CONTENT = HTML.format(head=STYLE, body=CONTENT_BODY)
    return HTMLResponse(CONTENT, status_code=exc.status_code)

EXCEPTION_HANDLERS = {
    404: not_found,
    500: server_error,
}

app = Starlette(
    debug=True,
    routes=ROUTES,
    exception_handlers=EXCEPTION_HANDLERS,
)
