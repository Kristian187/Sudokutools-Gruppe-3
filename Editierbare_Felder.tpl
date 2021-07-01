<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sudoku</title>
    <link rel="stylesheet" href="static/editierbare_felder.css">
</head>
    <div class="headline">
        <h1 font="sans-serif">Sudoku</h1>
    </div>
    <div class="game">
        <form action="/solve" , method="POST" name="grid" id="grid">
        <form action="/check" method="GET" name="grid_checker" id="grid_checker">
            % try:
                % for row in range(9):
                    % for column in range(9):
                        % pulse_class = ""
                        % if pulse_lists[row][column] == "pulse_red":
                            % pulse_class = "pulse_red"
                        % elif pulse_lists[row][column] == "pulse_green":
                            % pulse_class = "pulse_red"
                        % end
                    % end
                % end
            % except:
                % pass
            % end
            <div class="rand">
                % counter = 0
                % for x in range (9):
                    % for y in range (9):
                        % counter += 1
                        <div class="normalesdiv {{"rechterrand" if (y+1)%3==0 and (y+1)!=9 else ""}} {{"untererrand" if (x+1)%3==0 and (x+1)!=9 else ""}}">
                            <input class="sudoku_input" name="{{(x*9)+y}}" type= "text" maxlength="1" min="1" max="9" inputmode="numeric"
                            % if grid[x][y] !=0 and str(grid[x][y]).isnumeric():
                                readonly
                                value={{grid[x][y]}}
                                STYLE="color: dimgrey"
                            % elif grid[x][y] !=0:
                                value={{grid[x][y]}}
                                STYLE="color: dimgrey"
                            % end
                            >
                        </div>
                    % end
                % end
            </div>
        </form>
    <div class="knoepfe">
        <a href="/solve"><button name="reset_button" type="submit" form="grid">Solve</button></a>
        <a href="/create_example"><button name="reset_button" type="button">Create Example</button></a>
        <a href="/check"><button name="reset_button" type="button">Check</button></a>
        <a href="/"><button name="reset_button" type="button">Clear</button></a>
        <a href="einmalige_ausfuellung"><button name="name_button" type="button">Solve a Field</button></a>
    % try:
        % if value_error:
            <p>Only numbers are allowed!</p>
        % end
    % except:
        % pass
    % end
    </div>
</html>