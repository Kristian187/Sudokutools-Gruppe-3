from typing import List


# create and show
def init_empty_grid() -> List[List[int]]:
    """
    Just an empty grid.
    :return:Returns the empty grid.
    """
    return [[0] * 9 for x in range(9)]


def init_candidates() -> List[List[str]]:
    """
    Creates and returns the candidates template.
    :return: Returns the template for the candidates.
    """
    return [["123456789"] * 9 for x in range(9)]


def print_grid(grid: List[List[int]]):
    """
    Prints the grid for the Sudoku
    :param grid: This is a list of the Sudoku. Each list is a row in the Sudoku field.
    :return: There is no return.
    """
    for list_number in range(0, 9):
        for list_value in range(0, 9):
            if grid[list_number][list_value] == 0:
                print(end="  ")
            else:
                print(grid[list_number][list_value], end=" ")
            if list_value == 5 or list_value == 2:
                print("|", end=" ")
        print("")
        if list_number == 2 or list_number == 5:
            print("---------------------")


def set_default_sudoku_grid(grid: List[List[int]]):
    default_grid = [[0, 0, 1, 2, 0, 7, 0, 0, 0],
                    [0, 6, 2, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 9, 4, 0],
                    [0, 0, 0, 9, 8, 0, 0, 0, 3],
                    [5, 0, 0, 0, 0, 0, 0, 0, 0],
                    [7, 0, 0, 0, 3, 0, 0, 2, 1],
                    [0, 0, 0, 1, 0, 2, 0, 0, 0],
                    [0, 7, 0, 8, 0, 0, 4, 1, 0],
                    [3, 0, 4, 0, 0, 0, 0, 8, 0]]
    for x in range(9):
        for y in range(9):
            grid[x][y] = default_grid[x][y]


# Check00
def is_present_in_row(grid: List[List[int]], row_index: int, digit: int) -> bool:
    """
    Checks if the number in digit is already available in the row.
    :param grid: This is a list of the Sudoku. Each list is a row in the Sudoku field.
    :param row_index: This is the index for the rows in the Sudoku.
    :param digit: This is the digit that the program works with for the solution of the Sudoku.
    :return: Returns True or False
    """
    if digit in grid[row_index]:
        return True
    else:
        return False


def is_present_in_column(grid: List[List[int]], column_index: int, digit: int) -> bool:
    """
    Checks if the number in digit is already available in the column.
    :param grid: This is a list of the Sudoku. Each list is a row in the Sudoku field.
    :param column_index: This is the index for the columns in the Sudoku.
    :param digit: This is the digit that the program works with for the solution of the Sudoku.
    :return: Returns True or False
    """
    occurrence = 0
    for list_choice in range(9):
        if digit == grid[list_choice][column_index]:
            occurrence += 1
    if occurrence >= 1:
        return True
    else:
        return False


def is_present_in_block(grid: List[List[int]], row_index: int, column_index: int, digit: int) -> bool:
    pass


def is_possible_in_cell(grid: List[List[int]], row_index: int, column_index: int, digit: int) -> bool:
    """
    It checks if is_present_in_block or is_present_in_column or is_present_in_row is True and returns False, otherwise
    its True.
    :param grid: This is a list of the Sudoku. Each list is a row in the Sudoku field.
    :param row_index: This is the index for the rows in the Sudoku.
    :param column_index: This is the index for the columns in the Sudoku.
    :param digit: This is the digit that the program works with for the solution of the Sudoku.
    :return: It returns either True or False
    """
    if (is_present_in_block(grid, row_index, column_index, digit) or is_present_in_row(grid, row_index, digit) or
            is_present_in_column(grid, column_index, digit)) is True:
        return False
    else:
        return True


# Solve
def remove_impossible_candidates(grid: List[List[int]], candidates: List[List[str]]):
    """
    It removes the candidates in a string that cannot be entered in a specific field.
    :param grid: This is a list of the Sudoku. Each list is a row in the Sudoku field.
    :param candidates: This is a list of the possible candidates
                        that could be entered in a specific field in the Sudoku.
    :return: There is no return
    """
    for row_index in range(9):
        for column_index in range(9):
            if grid[row_index][column_index] != 0:
                candidates[row_index][column_index] = ""
                continue

            for digit in range(1, 10):
                if is_possible_in_cell(grid, row_index, column_index, digit) is False:
                    candidates[row_index][column_index] = candidates[row_index][column_index].replace(str(digit), "")


def set_value_in_cell_by_last_candidate(grid: List[List[int]], candidates: List[List[str]]) -> bool:
    """
    Checks if a value in candidates has the length of one and fills the "last candidate" into the grid.
    :param grid: This is a list of the Sudoku. Each list is a row in the Sudoku field.
    :param candidates: This is a list of the possible candidates
                        that could be entered in a specific field in the Sudoku.
    :return: It returns either True or False
    """
    changes = 0
    for row_index in range(9):
        for column_index in range(9):
            if len(candidates[row_index][column_index]) == 1:
                grid[row_index][column_index] = int(candidates[row_index][column_index])
                changes += 1
    if changes >= 1:
        return True
    else:
        return False


def find_lonely_candidate_in_row(candidates: List[List[str]], row_index: int, column_index: int):
    """
    This function checks if a specific number can be entered in a field by looking if only one number can be entered in
    this one field of the whole row and sets the candidate to that number.
    :param candidates: This is a list of the possible candidates
                        that could be entered in a specific field in the Sudoku.
    :param row_index: This is the index for the rows in the Sudoku.
    :param column_index: This is the index for the columns in the Sudoku.
    :return: There is no return.
    """
    for digit in candidates[row_index][column_index]:
        occurrence = 0
        for columns in range(9):
            if candidates[row_index][columns].__contains__(digit):
                occurrence += 1
        if occurrence == 1:
            candidates[row_index][column_index] = digit


def find_lonely_candidate_in_column(candidates: List[List[str]], row_index: int, column_index: int):
    """
    This function checks if a specific number can be entered in a field by looking if only one number can be entered in
    this one field of the whole column and sets the candidate to that number.
    :param candidates: This is a list of the possible candidates
                        that could be entered in a specific field in the Sudoku.
    :param row_index: This is the index for the rows in the Sudoku.
    :param column_index: This is the index for the columns in the Sudoku.
    :return: There is no return.
    """
    for digit in candidates[row_index][column_index]:
        occurrence = 0
        for list_choice in range(9):
            if candidates[list_choice][column_index].__contains__(digit):
                occurrence += 1
        if occurrence == 1:
            candidates[row_index][column_index] = digit


def find_lonely_candidate_in_block(candidates: List[List[str]], row_index: int, column_index: int):
    pass


def find_lonely_candidates(candidates: List[List[str]]):
    """
    Gives find_lonely_candidate_in_row, find_lonely_candidate_in_column
    and find_lonely_candidate_in_block the values they need to make them work
    :param candidates: This is a list of the possible candidates
                        that could be entered in a specific field in the Sudoku.
    :return: There is nothing to return.
    """
    for row_index in range(9):
        for column_index in range(9):
            find_lonely_candidate_in_row(candidates, row_index, column_index)
            find_lonely_candidate_in_column(candidates, row_index, column_index)
            find_lonely_candidate_in_block(candidates, row_index, column_index)


def main():
    """
    This is the main program where every function is listed and set in in the correct order. Also the grid and the
    candidate lists are initialized in here.
    :return: There is no return.
    """
    grid = init_empty_grid()
    set_default_sudoku_grid(grid)
    round = 1
    candidates = init_candidates()
    while True:
        print(f"Round: {round}\n")
        round += 1
        print_grid(grid)
        remove_impossible_candidates(grid, candidates)
        find_lonely_candidates(candidates)
        print("\n\n\n")
        if set_value_in_cell_by_last_candidate(grid, candidates) is False:
            break


if __name__ == "__main__":
    main()