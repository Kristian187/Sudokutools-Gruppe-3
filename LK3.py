from typing import List


# create and show
def init_empty_grid() -> List[List[int]]:
    """
    By Nico
    Creates a 2-Dimensional list filled with 0s.
    :return: The empty grid
    """
    return [[0] * 9 for x in range(9)]


def print_grid(grid: List[List[int]]):
    """
    By Nico
    Prints the whole grid with the special characters (-, |).
    :param grid: The whole grid in a 2-Dimensional list
    :return: /
    """
    end_string = ""
    for row_index in range(9):
        for column_index in range(9):
            if grid[row_index][column_index] != 0:
                end_string += str(grid[row_index][column_index]) + " "
            else:
                end_string += "  "
            if (column_index + 1) % 3 == 0 and column_index != 8:
                end_string += "| "
        end_string += "\n"
        if (row_index + 1) % 3 == 0 and row_index != 8:
            end_string += "---------------------\n"
    print(end_string)


def init_candidates() -> List[List[str]]:
    """
    By Emil
    Creates a 2-Dimensional list filled with strings that contain "123456789"s.
    :return: Candidates as a string in a 2-Dimensional list
    """
    return [["123456789"] * 9 for x in range(9)]


def input_sudoku(grid: List[List[int]]):
    """
    By Emil
    Let's the user enter values into the list, row by row.
    :param grid: The whole grid in a 2-Dimensional list
    :return: /
    """
    for row_index in range(9):
        number_index = 0
        row = input(f"Row {row_index+1}: ")
        for element in row:
            if element.isdigit():
                grid[row_index][number_index] = int(element)
                number_index += 1


def set_default_sudoku_grid(grid: List[List[int]]):
    """
    By Nico & Emil
    Sets the Sudoku grid to the example which is given by the Task
    :param grid: The whole grid in a 2-Dimensional list
    :return: /
    """
    grid[0] = [0, 0, 1, 2, 0, 7, 0, 0, 0]
    grid[1] = [0, 6, 2, 0, 0, 0, 0, 0, 0]
    grid[2] = [0, 0, 0, 0, 0, 0, 9, 4, 0]
    grid[3] = [0, 0, 0, 9, 8, 0, 0, 0, 3]
    grid[4] = [5, 0, 0, 0, 0, 0, 0, 0, 0]
    grid[5] = [7, 0, 0, 0, 3, 0, 0, 2, 1]
    grid[6] = [0, 0, 0, 1, 0, 2, 0, 0, 0]
    grid[7] = [0, 7, 0, 8, 0, 0, 4, 1, 0]
    grid[8] = [3, 0, 4, 0, 0, 0, 0, 8, 0]


# Check
def is_present_in_row(grid: List[List[int]], row_index: int, digit: int):
    """
    By Nico
    Checks if the given digit is present in the whole row.
    :param grid: The whole grid in a 2-Dimensional list
    :param row_index: The given row
    :param digit: The given digit
    :return: True, if the given digit is already in the row, otherwise False
    """
    for column_index in range(9):
        if digit == grid[row_index][column_index]:
            return True
    return False


def is_present_in_column(grid: List[List[int]], column_index: int, digit: int):
    """
    By Nico
    Checks if the given digit is present in the whole column.
    :param grid: The whole grid in a 2-Dimensional list
    :param column_index: The given column
    :param digit: The given digit
    :return: True, if the given digit is already in the column, otherwise False
    """
    for row_index in range(9):
        if digit == grid[row_index][column_index]:
            return True
    return False


def is_present_in_block(grid: List[List[int]], row_index: int, column_index: int, digit: int) -> bool:
    """
    By Emil
    Checks if the given digit is present in the same block.
    :param grid: The whole grid in a 2-Dimensional list
    :param row_index: The given row
    :param column_index: The given column
    :param digit: The given digit
    :return: True, if the given digit is already in the column, otherwise False
    """
    row_index //= 3
    column_index //= 3
    row_index *= 3
    column_index *= 3
    for column in range(column_index, column_index+3):
        for row in range(row_index, row_index+3):
            cell = grid[row][column]
            if cell == digit:
                return True
            else:
                pass
    return False


def is_possible_in_cell(grid: List[List[int]], row_index: int, column_index: int, digit: int) -> bool:
    """
    By Emil
    Combines is_present_in_row, is_present_in_column and is_present_in_block and gives back a bool.
    :param grid: The whole grid in a 2-Dimensional list
    :param row_index: The given row
    :param column_index: The given column
    :param digit: The given digit
    :return: False, if the given digit is present in either row, column or block, otherwise True
    """
    if is_present_in_row(grid, row_index, digit):
        return False
    elif is_present_in_column(grid, column_index, digit):
        return False
    elif is_present_in_block(grid, row_index, column_index, digit):
        return False
    return True


# Solve
def remove_impossible_candidates(grid: List[List[int]], candidates: List[List[str]]):
    """
    By Nico & Emil
    Removes all candidates, if the number in the grid is not a 0 or
    gets rid of candidates that are through the rules impossible.
    :param grid: The whole grid in a 2-Dimensional list
    :param candidates: Candidates as a string in a 2-Dimensional list
    :return: /
    """
    for row_index in range(9):
        for column_index in range(9):
            for number in range(1, 10):
                if grid[row_index][column_index] != 0:
                    candidates[row_index][column_index] = ""
                elif not (is_possible_in_cell(grid, row_index, column_index, number)):
                    cache = candidates[row_index][column_index].replace(str(number), "")
                    candidates[row_index][column_index] = candidates[row_index][column_index]\
                        .replace(candidates[row_index][column_index], cache)


def set_value_in_cell_by_last_candidate(grid: List[List[int]], candidates: List[List[str]]) -> bool:
    """
    By Emil
    Checks if a cell has only 1 candidate left and if place the number into the grid.
    :param grid: The whole grid in a 2-Dimensional list
    :param candidates: Candidates as a string in a 2-Dimensional list
    :return: True, if a candidate got placed into the grid, otherwise False
    """
    change_happened = 0
    for row_index in range(9):
        for column_index in range(9):
            if len(candidates[row_index][column_index]) == 1:
                change_happened = 1
                grid[row_index][column_index] = int(candidates[row_index][column_index])
    if change_happened == 1:
        return True
    return False


def find_lonely_candidate_in_row(candidates: List[List[str]], row_index: int, column_index: int):
    """
    By Nico
    Looks in the whole row if a number appears only once.
    :param candidates: Candidates as a string in a 2-Dimensional list
    :param row_index: The given row
    :param column_index: The given column
    :return: /
    """
    for x in range(len(candidates[row_index][column_index])):
        present = False
        for y in range(9):
            for z in range(len(candidates[row_index][y])):
                if candidates[row_index][column_index][x] == candidates[row_index][y][z] and y != column_index:
                    present = True
                    break
            if present:
                break
        if not present:
            candidates[row_index][column_index] = candidates[row_index][column_index][x]
            break


def find_lonely_candidate_in_column(candidates: List[List[str]], row_index: int, column_index: int):
    """
    By Nico
    Looks in the whole column if a number appears only once.
    :param candidates: Candidates as a string in a 2-Dimensional list
    :param row_index: The given row
    :param column_index: The given column
    :return: /
    """
    for x in range(len(candidates[row_index][column_index])):
        present = False
        for y in range(9):
            for z in range(len(candidates[y][column_index])):
                if candidates[row_index][column_index][x] == candidates[y][column_index][z] and y != row_index:
                    present = True
                    break
            if present:
                break
        if not present:
            candidates[row_index][column_index] = candidates[row_index][column_index][x]
            break


def find_lonely_candidate_in_block(candidates: List[List[str]], row_index: int, column_index: int):
    """
    By Nico & Emil
    Looks in the whole 3x3 block if a number appears only once.
    :param candidates: Candidates as a string in a 2-Dimensional list.
    :param row_index: The given row
    :param column_index: The given column
    :return: /
    """
    row = row_index // 3
    column = column_index // 3
    row *= 3
    column *= 3
    for x in range(len(candidates[row_index][column_index])):
        present = False
        for y in range(row, row + 3):
            for z in range(column, column + 3):
                for w in range(len(candidates[y][z])):
                    if candidates[row_index][column_index][x] == candidates[y][z][w]:
                        if y == row_index and z == column_index:
                            continue
                        present = True
                        break
                if present:
                    break
            if present:
                break
        if not present:
            candidates[row_index][column_index] = candidates[row_index][column_index][x]
            break


def find_lonely_candidates(candidates: List[List[str]]):
    """
    By Emil
    Combines and runs find_lonely_candidate_in_row, find_lonely_candidate_in_column and find_lonely_candidate_in_block
    for every cell in the grid so every candidate gets checked.
    :param candidates: Candidates as a string in a 2-Dimensional list
    :return: /
    """
    for row_index in range(9):
        for column_index in range(9):
            find_lonely_candidate_in_row(candidates, row_index, column_index)
            find_lonely_candidate_in_column(candidates, row_index, column_index)
            find_lonely_candidate_in_block(candidates, row_index, column_index)


def main(grid):
    """
    By Nico & Emil
    Combines all functions needed to solve the Sudoku. Prints every round the grid.
    :return: /
    """
    candidates = init_candidates()
    while True:
        remove_impossible_candidates(grid, candidates)
        find_lonely_candidates(candidates)
        if not set_value_in_cell_by_last_candidate(grid, candidates):
            return grid


if __name__ == "__main__":
    main()
