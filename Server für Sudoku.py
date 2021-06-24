from bottle import run, route, template, request, static_file
from LK3 import *
import copy

@route("/")
def sudoku():
    return template("Editierbare_Felder.tpl",
                      grid=[[0, 0, 1, 2, 0, 7, 0, 0, 0],
                          [0, 6, 2, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 9, 4, 0],
                          [0, 0, 0, 9, 8, 0, 0, 0, 3],
                          [5, 0, 0, 0, 0, 0, 0, 0, 0],
                          [7, 0, 0, 0, 3, 0, 0, 2, 1],
                          [0, 0, 0, 1, 0, 2, 0, 0, 0],
                          [0, 7, 0, 8, 0, 0, 4, 1, 0],
                          [3, 0, 4, 0, 0, 0, 0, 8, 0]]
                    )


@route("/solve", method="POST")
def solve_sudoku():
    default_grid = get_grid_from_forms(request.forms)
    grid_solveable = copy.deepcopy(default_grid)
    grid_solveable = main(grid_solveable)
    checker = True
    for x in range(9):
        for y in range(9):
            if not grid_solveable[x][y] == 0:
                checker = False
    return template("Editierbare_Felder.tpl",
                    checker = checker)

@route("/solution", method="GET")
def solve_sudoku():
    grid = [[0, 0, 1, 2, 0, 7, 0, 0, 0],
            [0, 6, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 9, 4, 0],
            [0, 0, 0, 9, 8, 0, 0, 0, 3],
            [5, 0, 0, 0, 0, 0, 0, 0, 0],
            [7, 0, 0, 0, 3, 0, 0, 2, 1],
            [0, 0, 0, 1, 0, 2, 0, 0, 0],
            [0, 7, 0, 8, 0, 0, 4, 1, 0],
            [3, 0, 4, 0, 0, 0, 0, 8, 0]]

    grid_solved = main(grid)
    return template("Editierbare_Felder.tpl",
                    grid =grid_solved)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static/')




def get_grid_from_forms(forms):
    """
    Reads the entered grid and returns it as a list of lists
    :param forms: form content sent with the request
    :return: TicTacToe Grid as List of Lists
    """
    grid = [[0] * 9 for x in range(9)]

    for x in range(9):
        for y in range(9):
            grid[x].append(forms.get(str(x+y)))

    return grid


run(debug=True, reloader=True)
