from os.path import join, dirname, realpath


# find if there are any duplicates in the input list
def are_duplicates(group):
    for num in group:
        if num == 0:  # for sudoku, 0 is counted as an empty space and can be ignored
            continue

        # get the repetitions of the current value
        repetitions = 0
        for number in group:
            if num == number:
                repetitions += 1

        # if there is more than one of a value, there are duplicates
        if repetitions > 1:
            return True

    return False


def is_valid(file_name):
    # use the os package to find the current directory
    home_dir = dirname(realpath(__file__))

    # open a board file
    board = open(join(home_dir, "sudoku", file_name), 'r')

    # get all the rows from the file (not including \n characters)
    rows = []
    for row in board.readlines():
        row = list(row)
        for i in range(len(row)):
            if row[i] == "\n":
                row.pop(i)
            else:
                row[i] = int(row[i])
        rows.append(row)

    # get all of the columns by combining all values with the same index from the rows
    columns = []
    for i in range(9):
        column = []
        for row in rows:
            column.append(row[i])
        columns.append(column)

    # get all of the boxes
    boxes = []
    for i in range(3):
        for j in range(3):
            box = []
            for k in range(3):
                for m in range(3):
                    box.append(rows[3*i + k][3*j + m])
            boxes.append(box)

    # if there are any duplicates the board is not valid
    valid_board = True
    for row in rows:
        if are_duplicates(row):
            valid_board = False

    for column in columns:
        if are_duplicates(column):
            valid_board = False

    for box in boxes:
        if are_duplicates(box):
            valid_board = False


    return valid_board
