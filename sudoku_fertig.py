from bottle import run, route, template, request, static_file


@route("/")
def sudoku():
    return template("Editierbare_Felder.tpl")


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static/')


run(debug=True, reloader=True)


