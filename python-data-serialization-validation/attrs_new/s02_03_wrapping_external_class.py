from functools import partial

import attr

hprint = partial(print, " \n#")


# our external class
class ExternalThing:

    def __init__(self, x: int) -> None:
        self.x = x


# wrap external class with attrs
SomeThing = attr.define(
    these={
        'x': attr.field()
    }
)(ExternalThing)


def main() -> None:
    thing = SomeThing(10)
    print(thing)


if __name__ == "__main__":
    main()
