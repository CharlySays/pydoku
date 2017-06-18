import random, math
from field import *


def generateGrid(grid, number):

    for i in range(0, 9):
        row = []
        for j in range(0, 9):
            row.append(Field('', ''))
        grid.append(row)

    random.seed()

    solvePuzzle(grid, 0, 0)
    removeNNumbers(grid, number)

def removeNNumbers(grid, numbers):
    while (numbers > 0):
        row = random.randint(0, 8)
        column = random.randint(0, 8)
        if grid[row][column].get_label() != '':
            grid[row][column].set_label('')
            numbers -= 1


def isValid(grid, row, column, number):
    sectorRow = 3 * math.floor(row / 3)
    sectorColumn = 3 * math.floor(column / 3)
    row2 = (row + 4) % 3
    row1 = (row + 2) % 3
    column1 = (column + 2) % 3
    column2 = (column + 4) % 3

    for i in range(0, 9):
        if grid[i][column].get_label() == number and row != i:
            return False

        if grid[row][i].get_label() == number and column != i:
            return False

    if grid[row1 + sectorRow][column1 + sectorColumn].get_label() == number:
        return False
    if grid[row2 + sectorRow][column1 + sectorColumn].get_label() == number:
        return False
    if grid[row1 + sectorRow][column2 + sectorColumn].get_label() == number:
        return False
    if grid[row2 + sectorRow][column2 + sectorColumn].get_label() == number:
        return False

    return True


def solvePuzzle(grid, row, column):

    if row < 9 and column < 9:
        if grid[row][column].get_label() != '':
            if (column + 1) < 9:
                return solvePuzzle(grid, row, (column + 1))
            else:
                return solvePuzzle(grid, (row + 1), 0)
        else:
            randomizedNumbers = []

            while randomizedNumbers.__len__()<9:
                randomNumber = random.randint(1, 9)
                if randomNumber not in randomizedNumbers:
                    randomizedNumbers.append(randomNumber)

            for i in range(0, 9):
                if isValid(grid, row, column, str(randomizedNumbers[i])):
                    grid[row][column].set_label(str(randomizedNumbers[i]))
                    if (column + 1) < 9:
                        if solvePuzzle(grid, row, column + 1):
                            return True
                        else:
                            grid[row][column].set_label('')

                    else:
                        if solvePuzzle(grid, row + 1, 0):
                            return True
                        else:
                            grid[row][column].set_label('')
        return False
    else:
        return True
