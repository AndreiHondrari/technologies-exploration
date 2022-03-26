from typing import Optional

import rx

from rx.disposable.booleandisposable import BooleanDisposable
from rx.core.observable.observable import Observable


def produce_stuff(
    observer: rx.typing.Observer[str],
    scheduler: Optional[rx.typing.Scheduler],
) -> rx.typing.Disposable:
    observer.on_next("Wingardium Leviosa")
    observer.on_next("Obliviate")
    observer.on_next("Expecto patronum")
    observer.on_next("Sectumsempra")
    observer.on_next("Expelliarmus")
    observer.on_completed()

    return BooleanDisposable()


def on_next_produced(val: str) -> None:
    print("VAL", val)


def on_error_produced(e: Exception) -> None:
    print("ERR", repr(e))


def on_completed() -> None:
    print("Complete !")


def main() -> None:
    source: Observable = rx.create(produce_stuff)
    source.subscribe(on_next_produced, on_error_produced, on_completed)


if __name__ == '__main__':
    main()
