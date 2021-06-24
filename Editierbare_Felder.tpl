<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="static/editierbare_felder.css">
</head>
    <div class="game">
        <form action="/" , method="GET">
            <div class="rand">
                % counter = 0
                % for x in range (1,10):
                    % for y in range (1,10):
                        % counter += 1
                        <div class="normalesdiv {{"rechterrand" if y%3==0 and y!=9 else ""}} {{"untererrand" if x%3==0 and x!=9 else ""}}">
                            <input class="sudoku_input" name="{{(y-1)+(x-1)}}" type= "text" maxlength="1" min="1" max="9" inputmode="numeric"
                            % if grid[x-1][y-1] !=0:
                                readonly
                                value={{grid[x-1][y-1]}}
                            % end
                            >
                        </div>
                    % end
                % end
            </div>

        </form>
        <a href="/solve"><button name="reset_button" type="button">Solve</button></a>
    </div>
</html>