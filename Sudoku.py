sudoku = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def sudoku_printer():
    for row in range(0, 9):
        print("")
        if row % 3 == 0 and row != 0:
            print("----------------------")
        for column in range(len(sudoku[row])):
            if column % 3 == 0 and column != 0:
                print("|", end=" ")
            print(sudoku[row][column], end=" ")

def checker(row, column, num):
    # Check Rows
    for i in range(0, 9):
        if sudoku[row][i] == num:
            return False

    # Check Columns
    for i in range(0, 9):
        if sudoku[i][column] == num:
            return False

    # Check Box
    row = (row // 3) * 3
    column = (column // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[row+i][column+j] == num:
                return False

    return True

def solver():
    for row in range(0,9):
        for column in range(0,9):
            if sudoku[row][column] == 0:
                for number in range(1,10):
                    if checker(row, column, number):
                        sudoku[row][column] = number
                        solver()
                        sudoku[row][column] = 0

                return

    sudoku_printer()
solver()