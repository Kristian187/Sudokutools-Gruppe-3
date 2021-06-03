<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="static/editierbare_felder.css">
</head>
    <div class="rand">
        <form action="/", method="get">
            % counter = 0
            % for x in range (1,10):
                % for y in range (1,10):
                    % counter += 1
                    <div class="normalesdiv {{"rechterrand" if y%3==0 and y!=9 else ""}} {{"untererrand" if x%3==0 and x!=9 else ""}}">
                        <input type= "text" maxlength="1" min="1" max="9" inputmode="numeric">
                    </div>
                % end
            % end
            <input type="submit"><br>
        </form>
    </div>
</body>
</html>