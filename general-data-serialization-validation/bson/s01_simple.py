import pprint
from functools import partial

import bson

hprint = partial(print, " \n#")


def main() -> None:
    hprint("Original")
    original = {
        'a': 12.34,
        'b': "potato",
        'c': [0xff, 0xcc],
        'd': 1234
    }
    pprint.pprint(original)

    hprint("Encoded")
    encoded = bson.dumps(original)
    pprint.pprint(encoded)
    encoded_hex_bytes = [f"{hex(k): <4}" for k in encoded]

    total_len = len(encoded_hex_bytes)
    i = 0
    PRINT_SIZE = 10
    while i < total_len:
        print(encoded_hex_bytes[i:i+PRINT_SIZE])
        i += PRINT_SIZE

    hprint("Decoded")
    decoded = bson.loads(encoded)
    pprint.pprint(decoded)


if __name__ == "__main__":
    main()
