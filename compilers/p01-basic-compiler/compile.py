#!python

import argparse

from library import compile


def main() -> None:
    parser = argparse.ArgumentParser(description="Compiles NemeXis source code")

    parser.add_argument("input_file", help="Source code to compile")
    parser.add_argument(
        "-output_file",
        "-o",
        dest="output_file",
        default="out.py",
        help="Target file for the compiled program",
    )

    arguments = parser.parse_args()

    compile(arguments.input_file, arguments.output_file)


if __name__ == "__main__":
    main()
