import string

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.routing import Route

INDEX_CONTENT_TEMPLATE = """
<html>
    <head>
        <style>
            body {
                margin: 50px;
                font-size: 25px;
            }

            .link1 {
                text-decoration: none;
                color: white;
            }
        </style>
    </head>
    <body>
        <a href="/" class="link1">
            <h1>Hello !</h1>
        </a>
        <hr>
        <p>The wood is light because it is not heavy</p>
        <a href="/something">Sample path link</a><br>
        <a href="/somethingelse">Sample path link 2</a>
        <p>$stuff</p>
    </body>
</html>
"""


async def index(request: Request) -> HTMLResponse:
    stuff = request.path_params.get('stuff', 'N/A')

    content_template = string.Template(INDEX_CONTENT_TEMPLATE)
    html_result = content_template.substitute({'stuff': stuff})
    return HTMLResponse(html_result)


ROUTES = [
    Route('/', index),
    Route('/{stuff}', index),
]

app = Starlette(
    debug=True,
    routes=ROUTES
)
