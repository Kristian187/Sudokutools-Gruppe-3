from bottle import run, route, template, request, static_file


@route("/")
def sudoku():
    return template("Editierbare_Felder.tpl",
                    grid=[["", "", 1, 2, "", 7, "", "", ""],
                          ["", 6, 2, "", "", "", "", "", ""],
                          ["", "", "", "", "", "", 9, 4, ""],
                          ["", "", "", 9, "", "", "", "", 3],
                          [5, "", "", "", "", "", "", "", ""],
                          [7, "", "", "", 3, "", "", 2, 1],
                          ["", "", "", 1, "", 2, "", "", ""],
                          ["", 7, "", 8, "", "", 4, 1, ""],
                          [3, "", 4, "", "", "", "", 8, ""]]
                    )


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static/')


run(debug=True, reloader=True)


