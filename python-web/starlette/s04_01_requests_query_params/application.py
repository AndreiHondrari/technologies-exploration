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
        </style>
    </head>
    <body>
        <h1>Hello !</h1>
        <hr>
        <p>The wood is light because it is not heavy</p>
        <a href="?stuff=hello%20to%20darkness">Sample query link</a><br>
        <a href="?stuff=The%20cake%20is%20a%20lie">Sample query link 2</a>
        <p>$stuff</p>
    </body>
</html>
"""


async def index(request: Request) -> HTMLResponse:
    stuff = request.query_params.get('stuff', default='N/A')

    content_template = string.Template(INDEX_CONTENT_TEMPLATE)
    html_result = content_template.substitute({'stuff': stuff})
    return HTMLResponse(html_result)


ROUTES = [
    Route('/', index),
]

app = Starlette(
    debug=True,
    routes=ROUTES
)
