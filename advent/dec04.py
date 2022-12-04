from util import aocio

day_input = aocio.get_day(3)


def check_overlap(left: tuple[int, int], right: tuple[int, int]) -> bool:
    if left[0] <= right[0]:
        lower = left
        upper = right
    else:
        lower = right
        upper = left

    return upper[1] <= lower[1]


def test_check_overlap():
    assert check_overlap((1, 3), (2, 3))
    assert check_overlap((3, 7), (1, 10))
    assert not check_overlap((2, 6), (1, 1))
    assert not check_overlap((1, 4), (6, 9))

#
# def part_one(raw_input):
#     total = 0
#     for pair in raw_input.split('\n'):
#         left, right = pair.split(',')
#         left = tuple(left.split('-'))