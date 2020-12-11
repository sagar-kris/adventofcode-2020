import copy

currSeatMap = 0
nextSeatMap = 0


def cleanUp(inputFile):
    inputFile = inputFile.strip('\n')
    inputFile = inputFile.strip()
    inputFile = inputFile.split('\n')
    inputFile = [elem.strip() for elem in inputFile]
    inputFile = [list(elem) for elem in inputFile]
    return inputFile


def checkXBounds(colIdx, loLim, hiLim):
    return True


def checkYBounds(rowIdx, loLim, hiLim):
    return True


def emptyRulesPart1(row, col):
    if currSeatMap[row - 1][col - 1] != '#' and currSeatMap[row - 1][col] != '#' and \
            currSeatMap[row - 1][col + 1] != '#' and currSeatMap[row][col + 1] != '#' and \
            currSeatMap[row + 1][col + 1] != '#' and currSeatMap[row + 1][col] != '#' and \
            currSeatMap[row + 1][col - 1] != '#' and currSeatMap[row][col - 1] != '#':
        nextSeatMap[row][col] = '#'


def occupiedRulesPart1(row, col):
    tempSeatCounter = 0
    tempSeatCounter += 1 if currSeatMap[row - 1][col - 1] == '#' else 0
    tempSeatCounter += 1 if currSeatMap[row - 1][col] == '#' else 0
    tempSeatCounter += 1 if currSeatMap[row - 1][col + 1] == '#' else 0
    tempSeatCounter += 1 if currSeatMap[row][col + 1] == '#' else 0
    tempSeatCounter += 1 if currSeatMap[row + 1][col + 1] == '#' else 0
    tempSeatCounter += 1 if currSeatMap[row + 1][col] == '#' else 0
    tempSeatCounter += 1 if currSeatMap[row + 1][col - 1] == '#' else 0
    tempSeatCounter += 1 if currSeatMap[row][col - 1] == '#' else 0

    if tempSeatCounter >= 4:
        nextSeatMap[row][col] = 'L'


# octant 1 (top left)
def o1Empty(row, col):
    tempRow, tempCol = row-1, col-1
    # loops until it hits a 'L', '#', or border
    while tempRow > 0 and tempCol > 0 and currSeatMap[tempRow][tempCol] == '.':
        tempRow -= 1
        tempCol -= 1
    return currSeatMap[tempRow][tempCol] != '#'


# octant 2 (top)
def o2Empty(row, col):
    tempRow, tempCol = row-1, col
    while tempRow > 0 and currSeatMap[tempRow][tempCol] == '.':
        tempRow -= 1
    return currSeatMap[tempRow][tempCol] != '#'


# octant 3 (top right)
def o3Empty(row, col):
    tempRow, tempCol = row-1, col+1
    while tempRow > 0 and tempCol < len(currSeatMap[0]) - 1 and currSeatMap[tempRow][tempCol] == '.':
        tempRow -= 1
        tempCol += 1
    return currSeatMap[tempRow][tempCol] != '#'


# octant 4 (right)
def o4Empty(row, col):
    tempRow, tempCol = row, col+1
    while tempCol < len(currSeatMap[0]) - 1 and currSeatMap[tempRow][tempCol] == '.':
        tempCol += 1
    return currSeatMap[tempRow][tempCol] != '#'


# octant 5 (bottom right)
def o5Empty(row, col):
    tempRow, tempCol = row+1, col+1
    while tempRow < len(currSeatMap) - 1 and tempCol < len(currSeatMap[0]) - 1 and \
            currSeatMap[tempRow][tempCol] == '.':
        tempRow += 1
        tempCol += 1
    return currSeatMap[tempRow][tempCol] != '#'


# octant 6 (bottom)
def o6Empty(row, col):
    tempRow, tempCol = row+1, col
    while tempRow < len(currSeatMap) - 1 and currSeatMap[tempRow][tempCol] == '.':
        tempRow += 1
    return currSeatMap[tempRow][tempCol] != '#'


# octant 7 (bottom left)
def o7Empty(row, col):
    tempRow, tempCol = row+1, col-1
    while tempRow < len(currSeatMap) - 1 and tempCol > 0 and currSeatMap[tempRow][tempCol] == '.':
        tempRow += 1
        tempCol -= 1
    return currSeatMap[tempRow][tempCol] != '#'


# octant 8 (left)
def o8Empty(row, col):
    tempRow, tempCol = row, col-1
    while currSeatMap[tempRow][tempCol] == '.' and tempCol > 0:
        tempCol -= 1
    return currSeatMap[tempRow][tempCol] != '#'


def emptyRulesPart2(row, col):
    if o1Empty(row, col) and o2Empty(row, col) and o3Empty(row, col) and \
            o4Empty(row, col) and o5Empty(row, col) and o6Empty(row, col) and \
            o7Empty(row, col) and o8Empty(row, col):
        nextSeatMap[row][col] = '#'


def occupiedRulesPart2(row, col):
    tempSeatCounter = 0
    tempSeatCounter += 1 if not o1Empty(row, col) else 0
    tempSeatCounter += 1 if not o2Empty(row, col) else 0
    tempSeatCounter += 1 if not o3Empty(row, col) else 0
    tempSeatCounter += 1 if not o4Empty(row, col) else 0
    tempSeatCounter += 1 if not o5Empty(row, col) else 0
    tempSeatCounter += 1 if not o6Empty(row, col) else 0
    tempSeatCounter += 1 if not o7Empty(row, col) else 0
    tempSeatCounter += 1 if not o8Empty(row, col) else 0

    # print(f'({row},{col}) {tempSeatCounter}')
    if tempSeatCounter >= 5:
        nextSeatMap[row][col] = 'L'


def mapStep(part):
    global currSeatMap
    global nextSeatMap

    currSeatMap = copy.deepcopy(nextSeatMap)

    if part == 1:
        for rowIdx in range(1, len(currSeatMap) - 1):
            for colIdx in range(1, len(currSeatMap[0]) - 1):  # avoid padding layer
                if currSeatMap[rowIdx][colIdx] == 'L':  # empty
                    emptyRulesPart1(rowIdx, colIdx)
                elif currSeatMap[rowIdx][colIdx] == '#':  # occupado
                    occupiedRulesPart1(rowIdx, colIdx)

    else:  # part == 2
        for rowIdx in range(1, len(currSeatMap) - 1):
            for colIdx in range(1, len(currSeatMap[0]) - 1):  # avoid padding layer
                if currSeatMap[rowIdx][colIdx] == 'L':
                    emptyRulesPart2(rowIdx, colIdx)
                elif currSeatMap[rowIdx][colIdx] == '#':
                    occupiedRulesPart2(rowIdx, colIdx)


def print2D(arr):
    [print(elem) for elem in arr]


def countOccupied(seatMap):
    occupiedCount = 0
    for row in currSeatMap:
        for col in row:
            if col == '#':
                occupiedCount += 1
    return occupiedCount


def main():
    global currSeatMap
    global nextSeatMap

    inp = open("./day11input.txt", 'r').read()
    nextSeatMap = cleanUp(inp)  # inp is a 2D list of chars (seats)
    # print(nextSeatMap)

    # pad sides with single layer of seats
    nextSeatMap = [['.'] + row + ['.'] for row in nextSeatMap]
    # pad top/bottom with single layer of seats
    nextSeatMap.insert(0, ['.'] * len(nextSeatMap[0]))
    nextSeatMap.append(['.'] * len(nextSeatMap[0]))

    # save a step 0 copy for part 2
    OGMap = copy.deepcopy(nextSeatMap)

    while currSeatMap != nextSeatMap:
        mapStep(1)
        # print()
        # print(f'curr seat map')
        # print(countOccupied(currSeatMap))
        # print2D(currSeatMap)

    # PART 1
    # stasis has been reached
    print(f'part 1: {countOccupied(currSeatMap)}')

    # PART 2
    # reset maps
    currSeatMap = 0
    nextSeatMap = OGMap

    while currSeatMap != nextSeatMap:
        mapStep(2)
        # print()
        # print(f'curr seat map')
        # print(countOccupied(currSeatMap))
        # print2D(currSeatMap)

    print(f'part 2: {countOccupied(currSeatMap)}')


if __name__ == '__main__':
    main()
