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

            body,textarea {
                color: white;
                background-color: #111;
            }

            form {
                width: 500px;
                display: flex;
                flex-flow: column;
                row-gap: 10px;
                padding: 10px;
                border: 1px solid #999;
            }

            button {
                width: 100px;
                padding: 15px;
                border: 1px solid #555;
                border-radius: 5%;
                background-color: #333;
                cursor: pointer;
                color: white;
                font-weight: 600;
            }

            button:hover {
                background-color: #444;
                color: green;
            }

            textarea {
                resize: none;
                width: 100%;
                height: 300px;
                border: 1px solid #444;
                outline: none;
                font-family: cursive;
            }

            textarea:focus {
                border: 1px solid green;
            }

            .form-row {
                flex: 1;
            }

            .link1 {
                text-decoration: none;
                color: white;
            }

            .center {
                display: flex;
                flex-flow: row;
                justify-content: center;
            }
        </style>
    </head>
    <body>
        <a href="/" class="link1">
            <h1>Hello !</h1>
        </a>
        <hr>
        <p>The wood is light because it is not heavy</p>
        <form action="" method="POST">
            <div class="form-row">
                <textarea name="sometext"></textarea>
            </div>
            <div class="form-row center">
                <button type="submit">Put it in</button>
            </div>
        </form>
        <p>Submitted previously: <br><br>$stuff</p>
    </body>
</html>
"""


async def index(request: Request) -> HTMLResponse:
    form_data = await request.form()
    print(form_data)

    stuff = form_data.get('sometext', 'N/A')

    content_template = string.Template(INDEX_CONTENT_TEMPLATE)
    html_result = content_template.substitute({'stuff': stuff})
    return HTMLResponse(html_result)


ROUTES = [
    Route('/', index, methods=["GET", "POST"]),
]

app = Starlette(
    debug=True,
    routes=ROUTES
)
