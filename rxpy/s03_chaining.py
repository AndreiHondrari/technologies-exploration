import rx

from typing import cast

from rx import operators as op
from rx.core.observable.observable import Observable


def main() -> None:
    source: Observable = rx.of(11, 22, 33, 44, 55, 66, 77, 88, 99)

    composed = source.pipe(
        op.map(lambda x: x * 2),
        op.filter(lambda x: cast(bool, (x < 100)))
    )

    composed.subscribe(lambda x: print(x))


if __name__ == '__main__':
    main()
