import string
import os
import pathlib

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.routing import Route, Mount
from starlette.exceptions import HTTPException
from starlette.staticfiles import StaticFiles

os.chdir(pathlib.Path(__file__).parent)

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

<div>$stuff</div>
"""

INDEX_CONTENT_TEMPLATE = HTML.format(head=STYLE, body=INDEX_BODY)


async def index(request: Request) -> HTMLResponse:
    # preproc
    current_path = pathlib.Path("my_files").absolute()
    listing = os.listdir(current_path)

    elements = ""
    for x in listing:
        elements += f"<li><a href=\"/some/{x}\" target=\"_blank\">{x}</a></li>"

    full_list = f"<ul>{elements}</ul>"

    # render
    content_template = string.Template(INDEX_CONTENT_TEMPLATE)
    html_result = content_template.substitute({'stuff': full_list})
    return HTMLResponse(html_result)


ROUTES = [
    Route('/', index),
    Mount('/some', app=StaticFiles(directory="my_files"), name="static"),
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
