
from starlette.types import Scope, Receive, Send
from starlette.responses import PlainTextResponse


async def app(
    scope: Scope,
    receive: Receive,
    send: Send
) -> None:
    print(scope)
    print(receive)
    print(send)

    scope['type'] = 'http'
    response = PlainTextResponse("Fear you shall not feel")
    await response(scope, receive, send)
