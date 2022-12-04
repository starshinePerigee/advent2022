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


# this is so excessive because I was hunting for bugs in the wrong place
@pytest.mark.parametrize(
    "left, right, result",
    [
        ([1, 2], [3, 4], False),
        ([1, 3], [1, 4], True),
        ([1, 1], [2, 2], False),
        ([2, 4], [1, 4], True),
        ([3, 4], [1, 6], True),
        ([1, 5], [2, 6], False),
        ([1, 4], [2, 2], True),
        ([10, 20], [11, 19], True),
        ([11, 12], [13, 14], False)
    ]
)
def test_check_overlap(left, right, result):
    assert check_overlap(left + right) is result
    assert check_overlap(right + left) is result


def part_one(raw_input):
    total = 0
    for pair in raw_input.split('\n'):
        entries = re.split('[-,]', pair)
        # the actual bug was not converting these to ints, which worked 980 times out of 100 :c
        entries = [int(e) for e in entries]
        total += int(check_overlap(entries))
    return total


def test_part_one():
    assert part_one(aocio.get_day(4, True)) == 2
    print("")
    print(part_one(aocio.get_day(4)))


def check_overlap_two(entries: list[int]) -> bool:
    left = entries[0:2]
    right = entries[2:4]
    if left[0] == right[0] or left[1] == right[1]:
        return True
    elif left[0] < right[0]:
        return right[0] <= left[1]
    else:
        return left[0] <= right[1]


@pytest.mark.parametrize(
    "left, right, result",
    [
        ([1, 2], [3, 4], False),
        ([1, 3], [1, 4], True),
        ([1, 1], [2, 2], False),
        ([2, 4], [1, 4], True),
        ([3, 4], [1, 6], True),
        ([1, 5], [2, 6], True),
        ([1, 4], [2, 2], True),
        ([1, 9], [2, 5], True),
        ([1, 4], [4, 9], True)
    ]
)
def test_check_overlap_two(left, right, result):
    assert check_overlap_two(left + right) is result
    assert check_overlap_two(right + left) is result


def part_two(raw_input):
    total = 0
    for pair in raw_input.split('\n'):
        entries = re.split('[-,]', pair)
        entries = [int(e) for e in entries]
        total += int(check_overlap_two(entries))
    return total


def test_part_two():
    assert part_two(aocio.get_day(4, True)) == 4
    print("")
    print(part_two(aocio.get_day(4)))
