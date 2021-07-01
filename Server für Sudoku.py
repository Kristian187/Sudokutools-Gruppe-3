from bottle import run, route, template, request, static_file
from LK3 import *
import copy
import random


@route("/")
def sudoku_grid():
    return template("Editierbare_Felder.tpl",
                    grid=[[0]*9 for x in range(9)])


@route("/solve", method="POST")
def solve_sudoku():
    gotten_grid, value_error = get_grid_from_forms(request.forms)
    grid_solveable = copy.deepcopy(gotten_grid)
    grid_solveable = main(grid_solveable)
    checker = True
    for x in range(9):
        for y in range(9):
            if not grid_solveable[x][y] == 0:
                checker = False
    if value_error == True:
        return template("Editierbare_Felder.tpl",
                        checker = checker,
                        grid=grid_solveable,
                        value_error=True)
    else:
        return template("Editierbare_Felder.tpl",
                        checker = checker,
                        grid=grid_solveable)

@route("/create_example", method="GET")
def create_example():
    return template("Editierbare_Felder.tpl",
                    grid=copy.deepcopy(create_random_sudoku()))


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static/')


def create_random_sudoku():
    while True:
        random_grid = [[0]*9 for x in range(9)]
        how_many_numbers = 0
        while how_many_numbers < 25:
            number = random.randint(1, 9)
            row = random.randint(0, 8)
            column = random.randint(0, 8)
            if not is_present_in_row(random_grid, row, number) and\
                    not is_present_in_column(random_grid, column, number) and\
                    not is_present_in_block(random_grid, row, column, number):
                random_grid[row][column] = number
                how_many_numbers += 1
        solveable = main(copy.deepcopy(random_grid))
        filled = True
        for row in range(9):
            for column in range(9):
                if not solveable[row][column] != 0:
                    filled = False
                    break
            if not filled:
                break
        for row in range(9):
            for column in range(9):
                number = solveable[row][column]
                if not (is_present_in_row(solveable, row, number) == 1 and
                        is_present_in_column(solveable, column, number) == 1 and
                        is_present_in_block(solveable, row, column, number) == 1):
                    filled = False
        if filled:
            break
    return random_grid


def get_grid_from_forms(forms, value_error=None):
    """
    Reads the entered grid and returns it as a list of lists
    :param forms: form content sent with the request
    :return: TicTacToe Grid as List of Lists
    """
    grid = [[] for x in range(9)]

    for x in range(9):
        for y in range(9):
            if forms.get(str((x*9)+y)):
                try:
                    grid[x].append(int(forms.get(str((x*9)+y))))
                except ValueError:
                    grid[x].append(forms.get(str((x*9)+y)))
                    value_error = True
            else:
                grid[x].append(0)
    return grid, value_error


run(debug=True, reloader=True)
