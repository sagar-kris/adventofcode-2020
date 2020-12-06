inp = 0


def cleanUp(inputFile):
    inputFile = inputFile.strip('\n')
    inputFile = inputFile.strip()
    inputFile = inputFile.split('\n\n')
    inputFile = [elem.strip() for elem in inputFile]
    inputFile = [elem.strip('\n') for elem in inputFile]
    inputFile = [elem.split('\n') for elem in inputFile]
    return inputFile


def main():
    global inp
    inp = open("./day6input.txt", 'r').read()
    inp = cleanUp(inp)

    # PART 1
    counter = 0
    for group in inp:
        tempSet = set()
        for person in group:
            for char in person:
                tempSet.add(char)
        counter += len(tempSet)
    print(f'part 1: {counter}')

    # PART 2
    counter = 0
    for group in inp:
        setPerson0 = set([char for char in group[0]])
        if len(group) == 1:
            counter += len(setPerson0)
            continue
        for personIdx, person in enumerate(group[1:]):
            tempSet = set([char for char in person])
            setPerson0 = tempSet.intersection(setPerson0)
            # for char in person:
            #     tempSet.add(char)
        counter += len(setPerson0)
    print(f'part 2: {counter}')


if __name__ == '__main__':
    main()
