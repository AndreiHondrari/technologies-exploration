from io import BytesIO

from functools import partial

import msgpack

hprint = partial(print, " \n#")


def main() -> None:
    bytes_stream = BytesIO()

    hprint("Original data")
    original = [0xaa, 0xbb, 0xcc, 0xff]
    print(original)

    hprint("Serialize")
    msgpack.pack(original, bytes_stream)

    bytes_stream.seek(0)
    print(bytes_stream.read())

    hprint("Decode")
    bytes_stream.seek(0)  # reset position
    decoded = msgpack.unpack(bytes_stream)
    print(decoded)


if __name__ == "__main__":
    main()
