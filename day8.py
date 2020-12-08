import copy

inp = 0
setInstrIdx = set()
instrIdx = 0
counter = 0


def cleanUp(inputFile):
    inputFile = inputFile.strip('\n')
    inputFile = inputFile.strip()
    inputFile = inputFile.split('\n')
    inputFile = [elem.strip() for elem in inputFile]
    inputFile = [elem.strip('\n') for elem in inputFile]
    inputFile = [elem.split() for elem in inputFile]
    # print(f'len is {len(inputFile)}')
    return inputFile


def part2Loop(inp2):
    # print('part2Loop')
    setInstrIdx2 = set()
    instrIdx2 = 0
    while instrIdx2 not in setInstrIdx2:
        setInstrIdx2.add(instrIdx2)
        if instrIdx2 >= len(inp2):
            return True
        currInstr, currDir, currAmt = inp2[instrIdx2][0], inp2[instrIdx2][1][0], int(inp2[instrIdx2][1][1:])
        if currInstr == 'nop':
            instrIdx2 += 1
        elif currInstr == 'acc':
            instrIdx2 += 1
            # if currDir == '+':
            #     counter += currAmt
            # else:
            #     counter -= currAmt
        elif currInstr == 'jmp':
            if currDir == '+':
                instrIdx2 += currAmt
            else:
                instrIdx2 -= currAmt
    return False


def main():
    global inp
    inp = open("./day8input.txt", 'r').read()
    inp = cleanUp(inp)  # result is array of formatted passports, each passport is array of fields
    # print(inp)

    # PART 1
    global setInstrIdx
    global instrIdx
    global counter

    while instrIdx not in setInstrIdx:
        setInstrIdx.add(instrIdx)
        currInstr, currDir, currAmt = inp[instrIdx][0], inp[instrIdx][1][0], int(inp[instrIdx][1][1:])
        if currInstr == 'nop':
            instrIdx += 1
        elif currInstr == 'acc':
            instrIdx += 1
            if currDir == '+':
                counter += currAmt
            else:
                counter -= currAmt
        elif currInstr == 'jmp':
            if currDir == '+':
                instrIdx += currAmt
            else:
                instrIdx -= currAmt
    print(f'part 1: {counter}')

    # PART 2
    for changedInstrIdx in range(len(inp)):
        # print(f'changed instr is {changedInstrIdx}')
        inpCopy = copy.deepcopy(inp)
        if inpCopy[changedInstrIdx][0] == 'acc':
            continue
        else:  # instr is 'nop' or 'jmp'
            if inpCopy[changedInstrIdx][0] == 'nop':
                inpCopy[changedInstrIdx][0] = 'jmp'
            else:   # instr is 'jmp'
                inpCopy[changedInstrIdx][0] = 'nop'
            boolVar = part2Loop(inpCopy)

            if boolVar:
                # REPEAT
                if inp[changedInstrIdx][0] == 'nop':
                    inp[changedInstrIdx][0] = 'jmp'
                else:
                    inp[changedInstrIdx][0] = 'nop'

                counter = 0
                instrIdx = 0
                while instrIdx < len(inp):
                    currInstr, currDir, currAmt = inp[instrIdx][0], inp[instrIdx][1][0], int(inp[instrIdx][1][1:])
                    if currInstr == 'nop':
                        instrIdx += 1
                    elif currInstr == 'acc':
                        if currDir == '+':
                            counter += currAmt
                        else:
                            counter -= currAmt
                        instrIdx += 1
                    elif currInstr == 'jmp':
                        if currDir == '+':
                            instrIdx += currAmt
                        else:
                            instrIdx -= currAmt
                print(f'part 2: {counter}')
                return


if __name__ == '__main__':
    main()
