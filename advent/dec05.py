import re
from collections import defaultdict

import pytest

from util import aocio


day_input = aocio.get_day(5)


class CrateStacks:
    @classmethod
    def load_string(cls, s):
        """Takes in a string of just the crates"""
        if re.match(r"\d", s):
            raise RuntimeError("Don't include the column labels lol")

        stacks = defaultdict(str)

        # split into lines and start at the bottom
        lines = s.split("\n")[::-1]
        # note that even the rightmost empty columns have spaces in our test data,
        for line in lines:
            for pos in range(0, len(line)//4):
                char = line[pos*4+1]
                if char != " ":
                    stacks[pos+1] += char

        return cls(dict(stacks))

    def __init__(self, dict_data):
        self.stacks = dict_data

    def nice_string(self):
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

    def __getitem__(self, item):
        return self.stacks[item]


@pytest.fixture
def demo_crates():
    test_input = aocio.get_day(5, True, trim=False)
    return test_input.split("\n 1")[0]


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