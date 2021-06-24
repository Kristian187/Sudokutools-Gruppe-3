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


@route("/solve", method="GET")
def solve_sudoku():
    default_grid = [[0, 0, 1, 2, 0, 7, 0, 0, 0],
            [0, 6, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 9, 4, 0],
            [0, 0, 0, 9, 8, 0, 0, 0, 3],
            [5, 0, 0, 0, 0, 0, 0, 0, 0],
            [7, 0, 0, 0, 3, 0, 0, 2, 1],
            [0, 0, 0, 1, 0, 2, 0, 0, 0],
            [0, 7, 0, 8, 0, 0, 4, 1, 0],
            [3, 0, 4, 0, 0, 0, 0, 8, 0]]
    grid_solved = copy.deepcopy(default_grid)
    grid_solved = main(grid_solved)
    return template("Editierbare_Felder.tpl",
                    grid = default_grid,
                    grid_solved = grid_solved)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static/')


run(debug=True, reloader=True)


def get_grid_from_forms(forms):
    """
    Reads the entered grid and returns it as a list of lists
    :param forms: form content sent with the request
    :return: TicTacToe Grid as List of Lists
    """
    grid = []
    for x in range(9):
        for y in range(9):
            grid[x].append(forms.get(str(x+y)))
    return grid


