inp = 0


def cleanUp(inputFile):
    inputFile = inputFile.strip('\n')
    inputFile = inputFile.strip()
    inputFile = inputFile.split('\n')
    inputFile = [elem.strip() for elem in inputFile]
    return inputFile


def main():
    global inp
    inp = open("./day5input.txt", 'r').read()
    inp = cleanUp(inp)  # inp is an array of 'FBLR' strings

    maxRes = 0
    rowDict, colDict = {}, {}

    for elem in inp:
        tempStr = ''
        for char in elem:  # convert 'FBLR' strings to binary strings
            tempStr += '1' if char in 'BR' else '0'
        row, col = tempStr[0:7], tempStr[7:]  # separate out row, col
        row, col = int(row, 2), int(col, 2)  # convert binary strings to int base 10

        # PART 1 -- find max of 8*row + col
        if (8 * row) + col > maxRes:
            maxRes = (8 * row) + col

        # PART 2 -- add rows, cols to respective frequency dicts
        if row in rowDict.keys():
            rowDict[row] += 1
        else:
            rowDict[row] = 1
        if col in colDict.keys():
            colDict[col] += 1
        else:
            colDict[col] = 1

    # PART 1
    print(f'part 1: {maxRes}')

    # PART 2
    rowList, colList = [], []
    [rowList.append(elem[0]) if elem[1] < 8 else None for elem in rowDict.items()]
    [colList.append(elem[0]) if elem[1] < 112 else None for elem in colDict.items()]
    print(f'part 2: rowList: {rowList}')
    print(f'\t\tcolList: {colList}')
    # visual inspection yields row == 75 and col == 3. So final ans = 8*75 + 3 = 603 for my input.


if __name__ == '__main__':
    main()
