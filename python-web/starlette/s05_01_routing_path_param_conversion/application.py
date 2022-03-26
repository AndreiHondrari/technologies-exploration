import string
import html
from typing import Optional, Any

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.routing import Route
from starlette.exceptions import HTTPException
from starlette.converters import Converter

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

INDEX_BODY = (f"""
{HEADER}
<p>The wood is light because it is not heavy</p>
<a href="/some/123">Some int</a><br>
<a href="/some/fawjifowaog">Some int (wrong)</a><br>
<a href="/someelse/66.77">Some float</a><br>
<a href="/formidable/A010055">Some something</a><br>
""")

INDEX_CONTENT_TEMPLATE = HTML.format(head=STYLE, body=INDEX_BODY)


async def index(request: Request) -> HTMLResponse:
    form_data = await request.form()
    print(form_data)

    stuff = form_data.get('sometext', 'N/A')

    content_template = string.Template(INDEX_CONTENT_TEMPLATE)
    html_result = content_template.substitute({'stuff': stuff})
    return HTMLResponse(html_result)

SOME_BODY = (f"""
{HEADER}
<h1>SOMETHING</h1>
<p>$stuff</p>
""")

SOME_CONTENT_TEMPLATE = HTML.format(head=STYLE, body=SOME_BODY)


async def some(request: Request) -> HTMLResponse:

    kek: Optional[Any] = request.path_params.get('kek', None)
    print("KEK_TYPE", type(kek))

    content_template = string.Template(SOME_CONTENT_TEMPLATE)
    html_result = content_template.substitute(
        {
            'stuff': f"KEK {kek} ( <code>{html.escape(str(type(kek)))}</code> )",
        }
    )
    return HTMLResponse(html_result)


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


ROUTES = [
    Route('/', index),
    Route('/some/{kek:int}', some),
    Route('/someelse/{kek:float}', some),
    Route('/formidable/{kek:float}', some),
]

EXCEPTION_HANDLERS = {
    404: not_found,
    500: server_error,
}

app = Starlette(
    debug=True,
    routes=ROUTES,
    exception_handlers=EXCEPTION_HANDLERS,
)
