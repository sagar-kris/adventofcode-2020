
inp = 0
treeCounter = 0
mapL, mapW = 0, 0


def cleanUp(inputFile):
    inputFile = inputFile.strip('\n')
    inputFile = inputFile.strip()
    inputFile = inputFile.split('\n')
    inputFile = [elem.strip() for elem in inputFile]
    return inputFile


def countTrees(colStep, rowStep):
    global treeCounter
    treeCounter = 0
    colIdx = 0
    for rowIdx in range(0, mapL, rowStep):
        if inp[rowIdx][colIdx] == '#':
            treeCounter += 1
        colIdx += colStep
        colIdx %= mapW
    return treeCounter


def main():
    # import data
    global inp
    inp = open("./day3input.txt", 'r').read()
    # clean up data
    inp = cleanUp(inp)

    global mapL, mapW
    mapL, mapW = len(inp), len(inp[0])

    print(f'part 1: number of trees is {countTrees(3,1)}')
    print(f'part 2: number of trees is {countTrees(1,1) * countTrees(3,1) * countTrees(5,1) * countTrees(7,1) * countTrees(1,2)}')


if __name__ == '__main__':
    main()
