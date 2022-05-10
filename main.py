import random


def generateBlankSudokuBroad():
    grid = [[0 for i in range(9)] for j in range(9)]
    return grid


def printSudokuBroad(sudokuBroad):
    counter = 0
    i = 0
    out = ""
    for row in sudokuBroad:
        out += f"{row[0]} {row[1]} {row[2]} | {row[3]} {row[4]} {row[5]} | {row[6]} {row[7]} {row[8]}\n"
        counter += 1
        if counter == 3 and i < 8:
            out += "------+-------+------\n"
            counter = 0
        i += 1
    print(out)


def findPossibleValues(sudokuBroad, row, col):
    possibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if sudokuBroad[row][i] in possibleValues:
            possibleValues.remove(sudokuBroad[row][i])
        if sudokuBroad[i][col] in possibleValues:
            possibleValues.remove(sudokuBroad[i][col])
    for i in range(3):
        for j in range(3):
            if sudokuBroad[row // 3 * 3 + i][col // 3 * 3 + j] in possibleValues:
                possibleValues.remove(sudokuBroad[row // 3 * 3 + i][col // 3 * 3 + j])
    return possibleValues


def findAllPossibleValues(sudokuBroad):
    possibleValues = []
    for row in range(len(sudokuBroad)):
        a = []
        for col in range(len(sudokuBroad[row])):
            if sudokuBroad[row][col] == 0:
                a.append(findPossibleValues(sudokuBroad, row, col))
            else:
                a.append([])

        possibleValues.append(a)
    return possibleValues


def findLowestPossibleValuePos(sudokuBroad):
    lowestPossibleValueNum = 10
    lowestPossibleValuePos = [0, 0]

    for row in range(len(sudokuBroad)):
        for col in range(len(sudokuBroad[row])):
            if sudokuBroad[row][col] == 0:
                if (
                    len(findPossibleValues(sudokuBroad, row, col))
                    < lowestPossibleValueNum
                ):
                    lowestPossibleValueNum = len(
                        findPossibleValues(sudokuBroad, row, col)
                    )
                    lowestPossibleValuePos = [row, col]

    return lowestPossibleValuePos


def isSolve(sudokuBroad):
    for row in sudokuBroad:
        if row.count(0) > 0:
            return False
    return True


for i in range(100):
    print(i)
    board = generateBlankSudokuBroad()
    while not isSolve(board):
        pos = findLowestPossibleValuePos(board)
        possibleValue = findPossibleValues(board, pos[0], pos[1])
        a = findAllPossibleValues(board)

        if len(possibleValue) > 0:
            value = random.choice(possibleValue)
            board[pos[0]][pos[1]] = value

        # collape board
        for row in range(len(board)):
            for col in range(len(board[row])):
                if len(findPossibleValues(board, row, col)) == 1:
                    board[row][col] = findPossibleValues(board, row, col)[0]

    printSudokuBroad(board)
