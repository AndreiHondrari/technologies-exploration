
import time
import math
import string
import random
import dataclasses as dc
from decimal import Decimal

from typing import List, Dict, Any, Protocol, cast

from test_packs import pack_cattrs, pack_drf, pack_pydantic

D = Decimal


class PackProtocol(Protocol):

    @staticmethod
    def structure(item_dict: Dict[str, Any]) -> Any: ...

    @staticmethod
    def destructure(item: Any) -> Dict[str, Any]: ...


@dc.dataclass(frozen=True)
class PackResults:
    """
    All values are represented in microseconds
    """
    structuring_times: List[int]
    best_structuring_time: float
    worst_structuring_time: float

    destructuring_times: List[int]
    best_destructuring_time: float
    worst_destructuring_time: float


def random_number() -> int:
    return random.randint(100_000, 999_999)


def random_string() -> str:
    return "".join(
        [random.sample(string.ascii_letters, 1)[0] for _ in range(500)]
    )


def generate_test_cases(amount: int = 100) -> List[Dict[str, Any]]:
    cases = []

    for _ in range(amount):
        new_case = {
            'x': random_number(),
            'y': random_number(),

            'a': random_number(),
            'b': random_number(),
            'c': random_number(),
            'd': random_number(),

            'descr': random_string(),

            'descr_a': random_string(),
            'descr_b': random_string(),

            'subitem_1': {
                'a': random_number(),
                'b': random_number(),
                'c': random_number(),
                'd': random_number(),
            },

            'collection': [
                {'f': random_number(), 'r': random_string()},
                {'f': random_number(), 'r': random_string()},
                {'f': random_number(), 'r': random_string()},
            ],

            'collection_2': [
                random_string(),
                random_string(),
                random_string(),
            ]
        }
        cases.append(new_case)

    return cases


def run_tests(
    pack: PackProtocol,
    test_cases: List[Dict[str, Any]]
) -> PackResults:

    structuring_times: List[int] = []
    best_structuring_time = math.inf
    worst_structuring_time = 0

    destructuring_times: List[int] = []
    best_destructuring_time = math.inf
    worst_destructuring_time = 0

    for case in test_cases:

        # structuring
        start = time.time_ns()
        item = pack.structure(case)
        stop = time.time_ns()
        duration_ns = stop - start
        duration_us = duration_ns // 1000
        best_structuring_time = min(best_structuring_time, duration_us)
        worst_structuring_time = max(worst_structuring_time, duration_us)
        structuring_times.append(duration_us)

        # destructuring
        start = time.time_ns()
        pack.destructure(item)
        stop = time.time_ns()
        duration_ns = stop - start
        duration_us = duration_ns // 1000
        best_destructuring_time = min(best_destructuring_time, duration_us)
        worst_destructuring_time = max(worst_destructuring_time, duration_us)
        destructuring_times.append(duration_us)

    return PackResults(
        structuring_times=structuring_times,
        best_structuring_time=best_structuring_time,
        worst_structuring_time=worst_structuring_time,
        destructuring_times=destructuring_times,
        best_destructuring_time=best_destructuring_time,
        worst_destructuring_time=worst_destructuring_time,
    )


def calculate_mean(
    values: List[int]
) -> Decimal:
    total = sum(values)
    return D(total) / D(len(values))


def calculate_variance(
    mean: Decimal,
    values: List[int],
) -> Decimal:
    numerator = sum([(x - mean) ** 2 for x in values])
    denominator = len(values) - 1
    return D(numerator) / D(denominator)


def standard_deviation(variance: Decimal) -> Decimal:
    return D(math.sqrt(variance))


SEPARATOR = "-" * 20


def display_pack_results(
    name: str,
    results: PackResults
) -> None:
    # calculate structuring indices
    # st_times_us = list(
    #     map(
    #         lambda x: x // 1_000,
    #         results.structuring_times
    #     )
    # )
    st_times_us = results.structuring_times

    st_mean_us = calculate_mean(st_times_us)
    st_variance_us = calculate_variance(
        st_mean_us, st_times_us
    )
    st_std_dev_us = standard_deviation(
        st_variance_us
    )

    # calculate destructuring indices
    # dest_times_us = list(
    #     map(
    #         lambda x: x // 1_000,
    #         results.destructuring_times
    #     )
    # )
    dest_times_us = results.destructuring_times

    dest_mean_us = calculate_mean(dest_times_us)
    dest_variance_us = calculate_variance(
        dest_mean_us, dest_times_us
    )
    dest_std_dev_us = standard_deviation(
        dest_variance_us
    )

    # display
    print("\n", SEPARATOR, sep="")
    print(f"RESULTS FOR {name}")
    print(SEPARATOR)

    print(" -- STRUCTURING --")
    print(
        "BEST (uS): {:.2f}".format(
            results.best_structuring_time
        )
    )
    print(
        "WORST (uS): {:.2f}".format(
            results.worst_structuring_time
        )
    )
    print("MEAN (uS): {:.2f}".format(st_mean_us))
    print("VARIANCE (uS): {:.2f}".format(st_variance_us))
    print("STD_DEVIATION (uS): {:.2f}".format(st_std_dev_us))

    print(" -- DESTRUCTURING --")
    print(
        "BEST (uS): {:.2f}".format(
            results.best_destructuring_time
        )
    )
    print(
        "WORST (uS): {:.2f}".format(
            results.worst_destructuring_time
        )
    )
    print("MEAN (uS): {:.2f}".format(dest_mean_us))
    print("VARIANCE (uS): {:.2f}".format(dest_variance_us))
    print("STD_DEVIATION (uS): {:.2f}".format(dest_std_dev_us))


def main() -> None:
    AMOUNT_OF_TEST_CASES = 1000

    ENABLED_PACKS = {
        "attrs+cattrs": pack_cattrs,
        "Pydantic": pack_pydantic,
        "Django REST Framework": pack_drf,
    }

    print("Generate test cases ...")
    test_cases = generate_test_cases(AMOUNT_OF_TEST_CASES)

    print("Run tests on all enabled packs ...")
    for pack_name, pack in ENABLED_PACKS.items():
        results: PackResults = run_tests(cast(PackProtocol, pack), test_cases)
        display_pack_results(pack_name, results)


if __name__ == "__main__":
    main()
