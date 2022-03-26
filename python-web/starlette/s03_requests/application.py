import string
import html
import pprint

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.routing import Route

INDEX_CONTENT = """
<html>
    <head>
        <style>
            body {
                margin: 50px;
                font-size: 25px;
                background-color: #1e1e1e;
                color: white;
            }

            a {color: green}
        </style>
    </head>
    <body>
        <h1>Hello !</h1>
        <hr>
        <p>The wood is light because it is not heavy</p>
        <a href="/some">Something</a>
    </body>
</html>
"""

SOME_CONTENT_TEMPLATE = """
<html>
    <head>
        <style>
            body {
                margin: 50px;
                font-size: 20px;
                font-family: sans-serif;
                background-color: #1e1e1e;
                color: white;
            }

            pre {
                padding: 0;
                margin: 0;
                width: 100%;
                white-space: pre-wrap;       /* css-3 */
                word-wrap: break-word;       /* Internet Explorer 5.5+ */
            }

            .key {
                color: green;
            }

            .val {
                color: blue;
            }

            .exc {
                color: red;
            }

            li {
                padding: 10px;
                margin-bottom: 10px;
                list-style-type: none;
                background-color: #333;
                transition: background-color 0.2s;
            }

            li:hover {
                background-color: #444;
            }
        </style>
    </head>
    <body>
        <h1>Hello !</h1>
        <hr>
        <div>$request_stuff</div>
    </body>
</html>
"""


async def index(request: Request) -> HTMLResponse:
    return HTMLResponse(INDEX_CONTENT)


async def some(request: Request) -> HTMLResponse:

    parts = "<ul>"

    for k in filter(lambda x: not x.startswith("_"), dir(request)):
        try:
            attribute = getattr(request, k)
            attr_string = pprint.pformat(attribute)
            attr_string = html.escape(attr_string)

            parts += """
                <li>
                    <span class="key">{}</span><br><br>
                    <pre class="val">{}</pre>
                </li>
            """.format(k, attr_string)

        except Exception as ex:
            parts += "<li class=\"exc\">EXCEPTION {} | {}</li>".format(k, str(ex))

    parts += "</ul>"

    content_template = string.Template(SOME_CONTENT_TEMPLATE)
    html_result = content_template.substitute({'request_stuff': parts})
    return HTMLResponse(html_result)


ROUTES = [
    Route('/', index),
    Route('/some', some),
]

app = Starlette(
    debug=True,
    routes=ROUTES
)
