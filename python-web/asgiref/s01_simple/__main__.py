from asgiref import server as asgi_server
# from asgiref import


async def application(scope, receive, send):
    event = await receive()

    body = "Hello world !"
    body_bytes = body.encode()

    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": [
            (b'Content-Type', b'text/html',),
            (b'Content-Length', str(len(body_bytes)).encode(),),
            # (b'', b'',),
        ]
    })

    await send({
        "type": "http.response.body",
        "body": body_bytes,
        "more_body": False,
    })


def main() -> None:
    print("START SERVER")

    instance = asgi_server.StatelessServer(application)
    try:
        instance.run()
    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    print("STOP SERVER")


if __name__ == "__main__":
    main()
