import pytest

from util import aocio


def parse_command(start: int, command: str) -> list[int]:
    if "noop" in command:
        return [start]
    else:
        opcode, num = command.split(" ")
        if opcode != "addx":
            raise RuntimeError(f"Invalid opcode: '{opcode}'")
        else:
            val = int(num.strip())
            return [start, start+val]


@pytest.mark.parametrize(
    "command, expected",
    [
        ("noop", 20),
        ("addx 4", 24),
        ("addx -10", 10)
    ]
)
def test_parse_command(command, expected):
    result = parse_command(20, command)
    if command == "noop":
        assert len(result) == 1
    else:
        assert len(result) == 2

    assert result[-1] == expected


def parse_all_commands(input_str: str) -> list[int]:
    commands = input_str.splitlines()
    signal = [1, 1]
    level = 1
    for command in commands:
        signal += parse_command(level, command)
        level = signal[-1]
    return signal


SMALL_TEST = """noop
addx 3
addx -5"""


@pytest.mark.parametrize(
    "command_string, target_points, is_test",
    [
        (SMALL_TEST, [(1, 1), (2, 1), (4, 4), (6, -1)], False),
        (aocio.get_day(10, True), [(20, 21), (60, 19), (100, 18), (140, 21), (180, 16), (220, 18)], True),
        (aocio.get_day(10), [], False)
    ],
    ids=["small", "test", "real"]
)
def test_parse_all(command_string, target_points, is_test):
    results = parse_all_commands(command_string)
    print("")
    for i, val in enumerate(results):
        print(f"{i:>3}: {val}")
    print("\n~ ~ ~ ~ ~\n")
    for target in target_points:
        print(f"{target[0]}: {results[target[0]]}")
        assert results[target[0]] == target[1]

    running_total = 0
    for i in range(20, len(results), 40):
        print(f"{i} * {results[i]} = {i * results[i]}")
        running_total += results[i] * i
    print(f"total total: {running_total}")
    if is_test:
        assert running_total == 13140