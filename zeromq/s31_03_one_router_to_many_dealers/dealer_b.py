
from dealer import run

DEALER_ROUTING_ID = (2).to_bytes(1, 'big')


def main() -> None:
    run(DEALER_ROUTING_ID)


if __name__ == "__main__":
    main()
