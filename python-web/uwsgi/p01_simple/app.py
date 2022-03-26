from wsgiref import headers as wsgi_headers
from typing import TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from _typeshed.wsgi import WSGIEnvironment, StartResponse


def application(
    environ: "WSGIEnvironment",
    start_response: "StartResponse"
) -> Iterable[bytes]:
    headers = wsgi_headers.Headers()
    headers.add_header('Content-Type', 'text/html')
    start_response('200 OK', headers.items())

    return [b'Bla ble blu']
