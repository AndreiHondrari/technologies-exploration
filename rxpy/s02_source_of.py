import rx

from rx.core.observable.observable import Observable


def main() -> None:
    source: Observable = rx.of(111, 222, 333, 444, 555)
    source.subscribe(lambda x: print(x))


if __name__ == '__main__':
    main()
