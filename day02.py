#!/usr/bin/env python
# from collections import Counter
from itertools import tee
from pathlib import Path
# from typing import Iterator


def part_one(path: Path) -> None:
    data = list(load_data(path))
    safe_reports = 0
    for report in data:
        if safety_checks(report):
            safe_reports += 1
    print(f"{safe_reports=}")


def part_two(path: Path) -> None:
    data = list(load_data(path))
    safe_reports = 0
    for report in data:
        # check if we pass the tests first time round
        if safety_checks(report):
            safe_reports += 1
        else:
            # check if we pass the tests by dropping one level
            for level_idx, level in enumerate(report):
                permutation = report.copy()
                del permutation[level_idx]
                if safety_checks(permutation):
                    # print(f" > safe by removing level at position={level_idx} {level} ({permutation=})")
                    safe_reports += 1
                    break
    print(f"{safe_reports=}")


def safety_checks(report: list[int]) -> bool:
    return safety_check_1(report) and safety_check_2(report)


def safety_check_1(levels: list[int]) -> bool:
    """The levels are either all increasing or all decreasing."""
    return levels == sorted(levels) or levels == sorted(levels, reverse=True)


def safety_check_2(levels: list[int]) -> bool:
    """Any two adjacent levels differ by at least one and at most three"""
    for a, b in pairwise(levels):
        if not 1 <= abs(b - a) <= 3:
            return False
    return True


# taken from: https://docs.python.org/3.3/library/itertools.html?highlight=pairwise
def pairwise(iterable: list[int]):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def load_data(path: Path):
    with path.open() as f:
        for line in f:
            if line.strip():
                yield [int(d) for d in line.strip().split()]


if __name__ == "__main__":
    path = Path("data/sample/day02.txt")
    # path = Path("data/day02.txt")
    part_one(path)
    # part_two(path)
