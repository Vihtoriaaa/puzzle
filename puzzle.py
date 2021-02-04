"""
Puzzle Game!!
"""


def check_rows(board):
    """
    list -> bool
    This function checks if every row has different numbers and returns
    True is yes, and False if not.
    >>> check_rows(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> check_rows(["**** ****", "***1 ****", "**  3****", "* 4 4****", \
"     9 5 ", " 6  83  *", "1   1  **", "  8  2***", "  2  ****"])
    False
    """
    for row in board:
        numbers = []
        for elem in row:
            if elem == '*' or elem == ' ':
                continue
            else:
                if elem in numbers:
                    return False
                numbers.append(elem)
    return True


def check_column(board):
    """
    list -> bool
    This function checks if every column has different numbers and returns
    True is yes, and False if not.
    >>> check_column(["**** ****", "***1 ****", "**  3****", \
"* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> check_column(["**** ****", "***1 ****", "**  3****", \
"* 4 1****", "     9 5 ", " 6  83  *", "3   5  **", "  8  2***", "  2  ****"])
    True
    """
    length = len(board)
    for i in range(length):
        one_line = []
        for line in board:
            if line[i] == '*' or line[i] == ' ':
                continue
            if line[i] in one_line:
                return False
            else:
                one_line.append(line[i])
    return True


def check_colors(board):
    """
    list -> bool
    This function gets lists of every colour's numbers and returns True if\
    every list has different digits and False if not.
    >>> check_colors(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> check_colors(["**** ****", "***1 ****", "**  9****", "* 4 1****", \
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    first_color = [line[4] for line in board[:5]]
    first_color = list(filter(lambda elem: elem != ' ', first_color))
    for i in range(5, 9):
        if board[4][i] != ' ':
            first_color.append(board[4][i])

    second_color = [line[3] for line in board[1:6]]
    second_color = list(filter(lambda elem: elem != ' ', second_color))
    for i in range(4, 8):
        if board[5][i] != ' ':
            second_color.append(board[5][i])

    third_color = [line[2] for line in board[2:7]]
    third_color = list(filter(lambda elem: elem != ' ', third_color))
    for i in range(3, 7):
        if board[6][i] != ' ':
            third_color.append(board[6][i])

    fourth_color = [line[1] for line in board[3:8]]
    fourth_color = list(filter(lambda elem: elem != ' ', fourth_color))
    for i in range(2, 6):
        if board[7][i] != ' ':
            fourth_color.append(board[7][i])

    fifth_color = [line[0] for line in board[4:9]]
    fifth_color = list(filter(lambda elem: elem != ' ', fifth_color))
    for i in range(1, 5):
        if board[8][i] != ' ':
            fifth_color.append(board[8][i])
    all_colours = [first_color, second_color, third_color, fourth_color,
        fifth_color]
    for colour in all_colours:
        if len(set(colour)) == len(colour):
            return True
        else:
            return False


def validate_board(board):
    """
    list -> bool
    This fucntion checks whether the puzzle board is ready to start the game
    depending on the rules.
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    if not check_colors(board) or not check_column(board) or not check_rows(board):
        return False
    return True
