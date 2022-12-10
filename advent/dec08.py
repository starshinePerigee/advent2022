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


def flip_matrix(matrix: list[list]) -> list[list]:
    return [x[::-1] for x in matrix]


def test_flip_matrix():
    m = [[1, 2, 3], [4, 5, 6]]
    assert m[0][0] == 1
    m = flip_matrix(m)
    assert m[0][0] == 3


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


def generate_one_directional_scenic(forest: list[list[int]]) -> list[list[int]]:
    scenic_matrix = []
    for row in forest:
        scenic_row = []
        for i, current_tree in enumerate(row):
            current_scenery = 0
            for j, col_item in enumerate(row):
                if i == j:
                    break
                elif col_item < current_tree:
                    current_scenery += 1
                else:
                    current_scenery = 1

            scenic_row += [current_scenery]
        scenic_matrix += [scenic_row]
    return scenic_matrix


def test_generate_one_directional_scenic():
    test_matrix = [
        [1, 2, 3],
        [3, 2, 1],
        [1, 3, 2]
    ]
    results = generate_one_directional_scenic(test_matrix)
    print("")
    print(stringify_matrix(results))
    assert results[0][0] == 0
    assert results[0][1] == 1
    assert results[0][2] == 2
    assert results[1][2] == 1


def test_generate_one_dimensional_scenic_real_data():
    test_input = aocio.get_day(8, True)
    test_forest = read_string(test_input)
    scenic = generate_one_directional_scenic(test_forest)
    print("")
    print(stringify_matrix(test_forest))
    print("")
    print(stringify_matrix(scenic))
    assert scenic[0][4] == 1
    assert scenic[0][3] == 3


def run_four_dimensional_scenic(forest):
    east = generate_one_directional_scenic(forest)

    flip_forest = flip_matrix(forest)
    west = generate_one_directional_scenic(flip_forest)
    west = flip_matrix(west)

    invert_forest = invert_2d_list(forest)
    north = generate_one_directional_scenic(invert_forest)
    north = invert_2d_list(north)

    invert_flip_forest = flip_matrix(invert_forest)
    south = generate_one_directional_scenic(invert_flip_forest)
    south = flip_matrix(south)
    south = invert_2d_list(south)

    total_scenic = []
    for row_east, row_west, row_north, row_south in zip(east, west, north, south):
        scenic_row = []
        for e, w, n, s in zip(row_east, row_west, row_north, row_south):
            scenic_row += [e * w * n * s]
        total_scenic += [scenic_row]
    return total_scenic


def get_2d_max(matrix):
    return max(max(row) for row in matrix)


@pytest.mark.parametrize(
    "text_input, is_test",
    [
        (aocio.get_day(8, True), True),
        (aocio.get_day(8), False)
    ],
    ids=["test", "real"]
)
def test_four_dimensional_scenic(text_input, is_test):
    print("")
    forest_matrix = read_string(text_input)
    final_scenic = run_four_dimensional_scenic(forest_matrix)
    print(stringify_matrix(final_scenic))
    if is_test:
        assert final_scenic[1][2] == 4
        assert get_2d_max(final_scenic) == 8
    else:
        print(f"best scenic score is {get_2d_max(final_scenic)}")