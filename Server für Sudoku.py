from bottle import run, route, template, request, static_file
from LK3 import *
import copy

@route("/")
def sudoku_grid():
    return template("Editierbare_Felder.tpl",
                      grid=[[0]*9 for x in range(9)])


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
                    checker = checker,
                    grid=grid_solveable)

@route("/create_example", method="GET")
def create_example():
    return template("Editierbare_Felder.tpl",
                    grid=[[0, 0, 1, 2, 0, 7, 0, 0, 0],
                        [0, 6, 2, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 9, 4, 0],
                        [0, 0, 0, 9, 8, 0, 0, 0, 3],
                        [5, 0, 0, 0, 0, 0, 0, 0, 0],
                        [7, 0, 0, 0, 3, 0, 0, 2, 1],
                        [0, 0, 0, 1, 0, 2, 0, 0, 0],
                        [0, 7, 0, 8, 0, 0, 4, 1, 0],
                        [3, 0, 4, 0, 0, 0, 0, 8, 0]])

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static/')




def get_grid_from_forms(forms):
    """
    Reads the entered grid and returns it as a list of lists
    :param forms: form content sent with the request
    :return: TicTacToe Grid as List of Lists
    """
    grid = [[] for x in range(9)]

    for x in range(9):
        for y in range(9):
            if forms.get(str((x*9)+y)):
                grid[x].append(int(forms.get(str((x*9)+y))))
            else:
                grid[x].append(0)
    return grid


run(debug=True, reloader=True)
