from util import aocio

day_input = aocio.get_day(3)


def parse_rucksack(s: str) -> int:
    half = int(len(s)/2)
    first_half = s[:half]
    second_half = s[half:]
    overlap = set([*first_half]) & set([*second_half])
    priority = ord(list(overlap)[0]) - ord('a') + 1
    # because ord(A) < ord(a), we need to reverse this:
    if priority < 0:
        priority = ord(list(overlap)[0]) - ord('A') + 27
    return priority


def part_one(input) -> int:
    return sum([parse_rucksack(s) for s in input.split("\n") if len(s) > 0])


def test_parse_rucksacks():
    assert parse_rucksack('vJrwpWtwJgWrhcsFMMfFFhFp') == 16
    assert parse_rucksack('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL') == 38


def test_part_one():
    assert part_one(aocio.get_day(3, True)) == 157
    print(part_one(aocio.get_day(3)))

