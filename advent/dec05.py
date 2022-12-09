import re
from collections import defaultdict

import pytest

from util import aocio


day_input = aocio.get_day(5)


class CrateStacks:
    @classmethod
    def load_string(cls, s: str) -> 'CrateStacks':
        """Takes in a string of just the crates"""
        if re.match(r"\d", s):
            raise RuntimeError("Don't include the column labels lol")

        stacks = defaultdict(str)

        # split into lines and start at the bottom
        lines = s.split("\n")[::-1]

        # note that even the rightmost empty columns have spaces in our test data,
        for line in lines:
            # turns out the real input doesn't have trailing spaces so add them to make the math work
            if len(line) % 4 != 0:
                line += " "
            for pos in range(0, len(line)//4):
                char = line[pos*4+1]
                if char != " ":
                    stacks[pos+1] += char

        return cls(dict(stacks))

    def __init__(self, dict_data: dict[str]):
        self.stacks = dict_data

    def nice_string(self) -> str:
        printstr = ""

        total_rows = max([len(x) for x in self.stacks.values()])
        for rank in range(total_rows, 0, -1):
            for col in self.stacks.values():
                if rank - 1 < len(col):
                    printstr += f"[{col[rank - 1]}] "
                else:
                    printstr += "    "
            printstr += "\n"

        for col_id in self.stacks.keys():
            printstr += f"{col_id:>2}  "

        return printstr

    def run_instruction(self, instruction: str) -> None:
        crunched = re.match(r"move (\d*) from (\d*) to (\d*)", instruction)

        if not crunched:
            raise RuntimeError(f"Invalid instruction: {instruction}")

        count, source, dest = map(int, crunched.groups())
        try:
            # moving = self[source][:-count-1:-1]
            # update for part 2
            moving = self[source][len(self[source]) - count:]
            self[source] = self[source][:-count]
            self[dest] = self[dest] + moving
        except KeyError:
            raise KeyError(f"Key error during instruction: {instruction}")

    def run_many_instructions(self, instructions: str) -> None:
        for instruction in instructions.splitlines():
            self.run_instruction(instruction)


    def __getitem__(self, item):
        return self.stacks[item]

    def __setitem__(self, key, value):
        self.stacks[key] = value


def split_file(full_input: str) -> tuple[str, str]:
    crate_section, remainder = full_input.split("\n 1")
    # we split on "move", so we have to put the first "move" back lol
    instruction_section = "move" + remainder.split("\nmove", maxsplit=1)[1]
    return crate_section, instruction_section


@pytest.fixture
def demo_crates():
    test_input = aocio.get_day(5, True, trim=False)
    return split_file(test_input)[0]


@pytest.fixture
def demo_stack(demo_crates):
    return CrateStacks.load_string(demo_crates)


def test_load(demo_crates, demo_stack):
    print("")
    print(demo_crates)
    assert (demo_crates[5]) is "D"

    assert demo_stack[1] == "ZN"
    assert demo_stack[2][2] == "D"


def test_init_print(demo_stack, demo_crates):
    nice_string = demo_stack.nice_string()
    print("\n" + nice_string)
    assert nice_string[:len(demo_crates)] == demo_crates


def test_run_instruction(demo_stack):
    demo_stack.run_instruction("move 1 from 2 to 1")
    assert demo_stack[1] == "ZND"
    assert demo_stack[2] == "MC"
    print("\n" + demo_stack.nice_string())


def test_run_second_half():
    crates, instructions = split_file(aocio.get_day(5, True, False))
    stack = CrateStacks.load_string(crates)
    stack.run_many_instructions(instructions)
    print("\n" + stack.nice_string())
    assert stack[1] == "M"
    assert stack[2] == "C"
    assert stack[3] == "PZND"

    # get answer
    s_crates, s_instructions = split_file(aocio.get_day(5, False, False))
    solution_stack = CrateStacks.load_string(s_crates)
    print(solution_stack.nice_string())
    print("~ ~ ~ ~")
    solution_stack.run_many_instructions(s_instructions)
    print(solution_stack.nice_string())
    final_str = [x[-1] for x in solution_stack.stacks.values()]

    print("".join(final_str))
