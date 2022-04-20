import pprint
from functools import partial

import something_pb2 as some

hprint = partial(print, " \n#")


def main() -> None:
    hprint("Define some messages")
    t1 = some.Thing()

    t1.title = "Kevin"
    t1.p = 123
    t1.bla = "Lolosaurus"

    it1 = t1.gags.add()
    it2 = t1.gags.add()

    it1.val = 3333
    it1.kek = t1.RED

    it2.val = 5555
    it2.kek = t1.TRANSPARENT

    print(t1)

    hprint("Serialize")
    encoded = t1.SerializeToString()
    print(encoded)

    hprint("Decode")
    decoded = t1.FromString(encoded)
    print(decoded)


if __name__ == "__main__":
    main()
