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
    inp = cleanUp(inp)  # inp is an array of groups. each group is an array of people responses (string).

    # PART 1
    counter = 0
    for group in inp:
        tempSet = set()
        for person in group:
            [tempSet.add(char) for char in person]
        counter += len(tempSet)
    print(f'part 1: {counter}')

    # PART 2
    counter = 0
    for group in inp:
        intersectSet = set([char for char in group[0]])
        for person in group[1:]:
            newSet = set([char for char in person])
            intersectSet = intersectSet.intersection(newSet)
        counter += len(intersectSet)
    print(f'part 2: {counter}')


if __name__ == '__main__':
    main()
