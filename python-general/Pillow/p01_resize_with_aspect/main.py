from PIL import Image


def main() -> None:
    original = Image.open('1.png')
    altered = original.copy()
    altered.thumbnail((1000, 1000), resample=None, reducing_gap=None)
    altered.show()


if __name__ == "__main__":
    main()
