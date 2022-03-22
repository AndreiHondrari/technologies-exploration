from http import HTTPStatus
from typing import TYPE_CHECKING, Iterable

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

if TYPE_CHECKING:
    from _typeshed.wsgi import StartResponse, WSGIEnvironment


def app(
    environ: "WSGIEnvironment",
    start_response: "StartResponse",
) -> Iterable[bytes]:
    # request = Request(environ)

    BODY = """
    <html>
        <head>
            <style>
                body {padding: 50px; font-size: 30px;}
            </style>
        </head>

        <body>
            <h1>HELLO !</h1>
            <hr>
            <p>A piece of wood that is not heavy, is light</p>
        </body>
    </html>
    """
    response = Response(
        BODY,
        status=HTTPStatus.OK,
        content_type='text/html',
    )
    return response(environ, start_response)


def main() -> None:
    run_simple(
        "127.0.0.1", 8080, app,
        use_reloader=True,
    )


if __name__ == "__main__":
    main()
