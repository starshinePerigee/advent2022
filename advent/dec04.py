import re

import pytest

from util import aocio

day_input = aocio.get_day(3)


def check_overlap(entries: list[int]) -> bool:
    left = entries[0:2]
    right = entries[2:4]
    if left[0] == right[0] or left[1] == right[1]:
        return True
    elif left[0] < right[0]:
        return right[1] < left[1]
    else:
        return left[1] < right[1]


@pytest.mark.parametrize(
    "left, right, result",
    [
        ([1, 2], [3, 4], False),
        ([1, 3], [1, 4], True),
        ([1, 1], [2, 2], False),
        ([2, 4], [1, 4], True),
        ([3, 4], [1, 6], True),
        ([1, 5], [2, 6], False)
    ]
)
def test_check_overlap(left, right, result):
    assert check_overlap(left + right) is result
    assert check_overlap(right + left) is result


def part_one(raw_input):
    total = 0
    for pair in raw_input.split('\n'):
        entries = re.split('[-,]', pair)
        total += int(check_overlap(entries))
    return total


def test_part_one():
    assert part_one(aocio.get_day(4, True)) == 2
    print("")
    print(part_one(aocio.get_day(4)))
