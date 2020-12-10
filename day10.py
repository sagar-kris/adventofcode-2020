inp = 0


def cleanUp(inputFile):
    inputFile = inputFile.strip('\n')
    inputFile = inputFile.strip()
    inputFile = inputFile.split('\n')
    inputFile = [int(elem.strip()) for elem in inputFile]
    return inputFile


def countOneIslands(fList, fDict):
    lo, hi = -1, 0  # lo has to start before first list index
    while hi < len(fList) - 1:
        hi = lo + 1 + fList[lo + 1:].index(3)  # find the next 3
        if hi - lo - 1 > 0:  # we don't care about 1 islands of length 0 (aka consecutive 3s)
            fDict[hi - lo - 1] += 1  # increment the count of the length of "1 island" found
        lo = hi
    return fDict


def main():
    global inp
    inp = open("./day10input.txt", 'r').read()
    inp = cleanUp(inp)  # inp is a list of ints
    inp = sorted(inp)  # joltages need to be in ascending order
    inp.insert(0, 0)  # wall is at 0 jolts
    inp.append(inp[-1] + 3)  # phone is at highest joltage + 3
    # print(inp)

    # PART 1
    diffList = []  # this will hold the difference of subsequent numbers
    for i in range(1, len(inp)):
        diffList.append(inp[i] - inp[i - 1])  # difference of subsequent numbers
    # print(diffList)

    count1s, count3s = diffList.count(1), diffList.count(3)
    print(f'part 1: {count1s * count3s}')

    # PART 2
    '''
    we need to find the number of "removable" 1s from resList.
    3s can never be removed because the joltage difference between adapters would be too high.
    a single 1 can never be removed -> 1 permutation
    with two consecutive 1s, the first one can be removed -> 2 permutations
    three consecutive 1s -> 4 permutations
    four consecutive 1s -> 7 permutations
    there are never more than four consecutive 1s in the input.
    '''
    permutationMapping = {1: 1, 2: 2, 3: 4, 4: 7}   # mapping of "1 island" lengths -> # of permutations
    onesDict = {1: 0, 2: 0, 3: 0, 4: 0}  # initialize dict. keys -> length of "1 islands"; values -> # of occurrences
    onesDict = countOneIslands(diffList, onesDict)
    # print(onesDict)

    numPermutations = 1
    for lenIsland in range(1, 5):
        numPermutations *= permutationMapping[lenIsland] ** onesDict[lenIsland]
    print(f'part 2: {numPermutations}')


if __name__ == '__main__':
    main()
