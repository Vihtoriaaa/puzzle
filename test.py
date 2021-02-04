from puzzle import validate_board

board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]

if __name__ == "__main__" :
    if validate_board(board) == False :
        print('Everything works fine!')
    else :
        print("Something goes wrong!")