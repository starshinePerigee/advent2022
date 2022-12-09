import pytest

from util import aocio


def find_first_packet(s: str, n: int) -> int:
    for i in range(len(s)):
        # this is a kind-of-hack: python converst a string into a set of characters
        if len(set(s[i:i+n])) == n:
            return i + n
    raise RuntimeError("Could not find unique four characters!")


@pytest.mark.parametrize(
    "input_string, position",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ]
)
def test_first_half(input_string, position):
    assert find_first_packet(input_string, 4) == position


def test_run_first_half():
    test_set = aocio.get_day(6)
    print(f"\nAnswer: {find_first_packet(test_set, 4)}")


@pytest.mark.parametrize(
    "input_string, position",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)
    ]
)
def test_second_half(input_string, position):
    assert find_first_packet(input_string, 14) == position


def test_run_second_half():
    test_set = aocio.get_day(6)
    print(f"\nAnswer: {find_first_packet(test_set, 14)}")
