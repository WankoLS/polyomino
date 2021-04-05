from copy import deepcopy as copy
from utils import *

def grid_rotate(grid):
    w = len(grid[0]) #new grid height
    h = len(grid) #new grid width
    result = []
    for c in range(w): #build a new row for each column in original
        newrow = []
        for r in range(h):
            newrow.append(grid[h-r-1][c])
        result.append(newrow)
    return result

def grid_reflect(grid):
    return grid[::-1] #vertical reflection is easier to write

def grid_pad(grid,left,top,width,height):
    curr_width = len(grid[0])
    curr_height = len(grid)

    new = []
    for r in range(height):
        if r < top or r >= curr_height + top:
            new.append([0] * width)
        else:
            row = [0] * left
            row += grid[r-top]
            row += [0] * (width - curr_width - left)
            new.append(row)
    return new

def grid_merge(g1,g2):
    new = []
    for r in range(len(g1)):
        newrow = []
        for c in range(len(g1[0])):
            if g1[r][c] != ".":
                newrow.append(g1[r][c])
            else:
                newrow.append(g2[r][c])
        new.append(newrow)
    return new


def checkCollision(g1, g2):
    # assume same dimensions
    for r in range(len(g1)):
        for c in range(len(g1[0])):
            if (g1[r][c] != ".") and (g2[r][c] != "."):
                return True
    return False


def allOrientations(penta):
    found = []
    current = copy(penta)

    while current not in found:
        cp = copy(current)
        found.append(cp)

        current = grid_rotate(current)

    current = grid_reflect(current)

    while current not in found:
        cp = copy(current)
        found.append(cp)

        current = grid_rotate(current)

    return found


def allPositions(penta, width, height):
    found = []
    for grid in allOrientations(penta):
        curr_width = len(grid[0])
        curr_height = len(grid)

        for c in range(0, width - curr_width + 1):
            for r in range(0, height - curr_height + 1):
                found.append(grid_pad(grid, c, r, width, height))
    return found


pentaPositions = {}


def dictionarySetup(pentas, penta_letters, m1, m2):

    for i in range(len(pentas)):
        modifiedPositions = []

        for pos in allPositions(pentas[i], m1, m2):
            newgrid = []
            for row in pos:
                newrow = []
                for cell in row:
                    if cell == 1:
                        newrow.append(penta_letters[i])
                    else:
                        newrow.append(".")
                newgrid.append(newrow)
            modifiedPositions.append(newgrid)

        pentaPositions[penta_letters[i]] = modifiedPositions


def tryFit(grid, pentas):
    #     print("Trying to fit " + str(pentas))
    #     print(grid)

    # nothing left to fit, done!
    if pentas == []:
        return grid

    next_penta = pentas[0]
    next_positions = pentaPositions[next_penta]

    for pos in next_positions:
        if not checkCollision(grid, pos):
            fit = tryFit(grid_merge(grid, pos), pentas[1:])
            if fit != None:
                return fit


def buildPentaList(numPenta, pentasUsed, remainingPentas, grid):
    # numPenta: remaining number of pentas we want
    # pentasUsed: list of pentas so far
    # remainingPentas: unused pentas
    # grid: grid we want to tile

    impossibles = []

    if numPenta == 0:
        result = tryFit(grid, pentasUsed)
        if result == None:
            return ["".join(pentasUsed)]  # found a set with no valid tiling

    if remainingPentas == []:
        return []  # nothing left to pull from, move on

    for i in range(len(remainingPentas)):
        result = buildPentaList(numPenta - 1, pentasUsed + [remainingPentas[i]], remainingPentas[i + 1:], grid)
        if result != None:
            impossibles += result
    return impossibles


