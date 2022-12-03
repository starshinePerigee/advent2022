from util import aocio

day_input = aocio.get_day(3)


def prioritize(c: str) -> int:
    priority = ord(c) - ord('a') + 1
    # because ord(A) < ord(a), we need to reverse this:
    if priority < 0:
        priority = ord(c) - ord('A') + 27
    return priority


def parse_rucksack(s: str) -> str:
    half = int(len(s)/2)
    first_half = s[:half]
    second_half = s[half:]
    overlap = {*first_half} & {*second_half}
    return list(overlap)[0]


def part_one(input) -> int:
    return sum([prioritize(parse_rucksack(s)) for s in input.split("\n") if len(s) > 0])


def test_parse_rucksacks():
    assert prioritize(parse_rucksack('vJrwpWtwJgWrhcsFMMfFFhFp')) == 16
    assert prioritize(parse_rucksack('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL')) == 38


def test_part_one():
    assert part_one(aocio.get_day(3, True)) == 157
    print(f"\npart 1: {part_one(aocio.get_day(3))}")


BADGE_TEST_1 = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
"""

BADGE_TEST_2 = """
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def parse_badges(r: list[str]) -> str:
    sets = [{*s} for s in r]
    overlap = sets[0] & sets[1] & sets[2]
    return list(overlap)[0]


def test_parse_badges():
    assert parse_badges(BADGE_TEST_1.strip().split('\n')) == 'r'
    assert parse_badges(BADGE_TEST_2.strip().split('\n')) == 'Z'


def part_two(input: str) -> int:
    # time to bust out an honest to god old school for loop
    lines = input.strip().split('\n')
    total = 0
    for i in range(0, len(lines), 3):
        badge = parse_badges(lines[i:i+3])
        total += prioritize(badge)
    return total


def test_part_two():
    print(f"\npart 2: {part_two(aocio.get_day(3))}")
