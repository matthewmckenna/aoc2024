#!/usr/bin/env python
from collections import Counter
from pathlib import Path
from typing import Iterator


def yield_ints(path: Path) -> Iterator[tuple[int, int]]:
    """Yield pairs of integers from a filepath"""
    with path.open() as f:
        for line in f:
            if line.strip():
                first, second = line.strip().split()
                yield int(first), int(second)


def part_one(path: Path) -> None:
    first, second = load_and_split_data(path)
    total = calculate_total_abs_difference(sorted(first), sorted(second))
    print(f"{total=}")


def part_two(path: Path) -> None:
    first, second = load_and_split_data(path)
    total = calculate_similarity_score(first, Counter(second))
    print(f"{total=}")


def calculate_similarity_score(
    identifiers: list[int], frequency: Counter[int, int]
) -> int:
    total = 0
    for identifier in identifiers:
        total += abs(identifier * frequency.get(identifier, 0))
    return total


def calculate_total_abs_difference(first: list[int], second: list[int]) -> int:
    """Calculate the total absolute difference between two lists"""
    total = 0
    for first_, second_ in zip(first, second):
        total += abs(first_ - second_)
    return total


def load_and_split_data(path: Path) -> tuple[list[int], list[int]]:
    """Load the data from a file and split it into two lists"""
    data = list(yield_ints(path))
    first, second = list(zip(*data))
    return first, second


if __name__ == "__main__":
    path = Path("data/sample/day01.txt")
    # path = Path("data/day01.txt")
    part_one(path)
    # part_two(path)
