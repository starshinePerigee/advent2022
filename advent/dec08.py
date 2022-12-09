import pytest

from util import aocio


def read_string(s: str) -> list[list[int]]:
    return [
        [int(x) for x in list(row.strip())]
        for row
        in s.splitlines()
    ]


def stringify_matrix(l: list[list]):
    print_str = ""
    for row in l:
        for col in row:
            print_str += str(col)[0]
        print_str += "\n"
    return print_str


def generate_visible_mask(matrix: list) -> list[list[bool]]:
    return [[False for x in row] for row in matrix]


def invert_2d_list(old_list: list[list]) -> list[list]:
    new_list = [[] for __ in range(len(old_list[0]))]
    for row in old_list:
        for i, col_item in enumerate(row):
            new_list[i] += [col_item]
    return new_list


def test_invert_2d_list():
    old_list = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    assert old_list[1][1] == 5
    print("")
    print(stringify_matrix(old_list))
    new_list = invert_2d_list(old_list)
    assert new_list[1][1] == 5
    print(stringify_matrix(new_list))


def test_read_string():
    matrix = read_string(aocio.get_day(8, True))
    print("")
    print(stringify_matrix(matrix))
    assert matrix[2][3] == 3


def test_visible_matrix():
    matrix = read_string(aocio.get_day(8, True))
    visible = generate_visible_mask(matrix)
    print("")
    print(stringify_matrix(visible))
    assert len(matrix) == len(visible)


def mark_all_visible_horizontal(forest: list[list[int]], visible: list[list[bool]]) -> list[list[bool]]:
    for y, row in enumerate(forest):
        lowest_tree = -1
        for x, col_item in enumerate(row):
            if col_item > lowest_tree:
                lowest_tree = col_item
                visible[y][x] = True

        # now do it the other way
        lowest_tree = -1
        for x, col_item in enumerate(row[::-1]):
            if col_item > lowest_tree:
                lowest_tree = col_item
                visible[y][len(row) - x - 1] = True

    return visible


@pytest.mark.parametrize(
    "text_input, is_test",
    [
        (aocio.get_day(8, True), True),
        (aocio.get_day(8), False)
    ],
    ids=["test", "real"]
)
def test_part_one(text_input, is_test):
    print("")
    forest_matrix = read_string(text_input)
    print(stringify_matrix(forest_matrix))

    visible_matrix = generate_visible_mask(forest_matrix)
    visible_matrix = mark_all_visible_horizontal(forest_matrix, visible_matrix)
    visible_matrix = invert_2d_list(visible_matrix)
    forest_matrix = invert_2d_list(forest_matrix)
    visible_matrix = mark_all_visible_horizontal(forest_matrix, visible_matrix)

    visible_matrix = invert_2d_list(visible_matrix)
    print(stringify_matrix(visible_matrix))
    total_visible = sum([sum(row) for row in visible_matrix])
    if is_test:
        assert total_visible == 21
    else:
        print(f"total: {total_visible}")
