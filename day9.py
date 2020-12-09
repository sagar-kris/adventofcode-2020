
inp = 0


def cleanUp(inputFile):
    inputFile = inputFile.strip('\n')
    inputFile = inputFile.strip()
    inputFile = inputFile.split('\n')
    inputFile = [int(elem.strip()) for elem in inputFile]
    return inputFile


def twoSumExists(inpList, targetSum):
    for elemIdx, elem in enumerate(inpList):
        if targetSum - elem in inpList[0:elemIdx] + inpList[elemIdx + 1:]:
            return True
    return False


def main():
    global inp
    inp = open("./day9input.txt", 'r').read()
    inp = cleanUp(inp)  # inp is an
    # print(len(inp))

    # PART 1
    streamLen = 25
    for i in range(streamLen, len(inp)):
        stream = inp[i - streamLen:i]
        currNum = inp[i]
        if twoSumExists(stream, currNum):
            continue
        # twoSum failed
        print(f'part 1: {currNum}')
        break

    # PART 2
    lo, hi = 0, 2
    while hi < len(inp):
        tempSum = sum(inp[lo:hi])
        if tempSum == currNum:
            break
        elif tempSum < currNum:
            hi += 1
        else:   # tempSum > currNum, so shring the range from the bottom
            lo += 1
    print(f'part 2: {min(inp[lo:hi]) + max(inp[lo:hi])}')


if __name__ == '__main__':
    main()
