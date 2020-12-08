import re

inp = 0
bagDict2 = {}
counter = 0


def cleanUp(inputFile):
    inputFile = inputFile.strip('\n')
    inputFile = inputFile.strip()
    inputFile = inputFile.split('\n')
    inputFile = [elem.split(' bags contain ') for elem in inputFile]
    # inputFile = [[elem, elem[1].split(', ')] for elem in inputFile]
    return inputFile


def countChildren(currBag):
    smallerBagsDict = bagDict2[currBag]
    # totalSmallerBags = sum(list(smallerBagsDict.values()))
    # counter += totalSmallerBags
    return [sum(int(smallBagQuantity) * countChildren(smallBagType), int(smallBagQuantity)) for smallBagType, smallBagQuantity in smallerBagsDict.items()]
    # for item in smallerBagsDict.items():
    #     return [
    #      list(smallerBagsDict.values())[1] * countChildren(list(smallerBagsDict.values())[0])


def main():
    global inp
    inp = open("./day7input.txt", 'r').read()
    inp = cleanUp(inp)  # inp is an
    # print(inp)

    # PART 1
    bagDict = {}  # source bag "can be inside" target bag

    for elem in inp:
        targetBag = elem[0]
        sourceBags = elem[1]
        sourceBags = re.split(' bag.| bags.| bag, [1-9] | bags, [1-9] |[1-9] ', sourceBags)
        [sourceBags.remove(garbo) if len(garbo) < 3 else None for garbo in sourceBags]
        # print(targetBag, sourceBags)

        for sourceBag in sourceBags:
            if sourceBag not in bagDict.keys():
                bagDict[sourceBag] = set()
            bagDict[sourceBag].add(targetBag)

    # print(bagDict)

    shinyGoldSet = set()
    q = ['shiny gold']
    while q:
        curr = q.pop()
        shinyGoldSet.add(curr)
        if curr in bagDict.keys():
            for bag in bagDict[curr]:
                q.append(bag)
    print(f'part 1: {len(shinyGoldSet) - 1}')

    # PART 2
    global bagDict2

    # construct dict of bags: bags inside them
    for elem in inp:
        bigBag = elem[0]
        littleBags = elem[1]
        littleBags = re.split(' bag.| bags.| bag, | bags, ', littleBags)
        [littleBags.remove(garbo) if len(garbo) < 3 else None for garbo in littleBags]
        littleBags = [garbo.strip(',') for garbo in littleBags]
        littleBags = [garbo.strip() for garbo in littleBags]
        # print(bigBag, littleBags)

        if bigBag not in bagDict2.keys():
            bagDict2[bigBag] = {}  # dict

        for littleBag in littleBags:
            # print(littleBag)
            tempEntry = littleBag.split(' ', 1)
            # print(tempEntry)
            if tempEntry[0] != 'no':
                numBags = int(tempEntry[0])
                bagType = tempEntry[1]

                bagDict2[bigBag][bagType] = numBags

    # print(bagDict2)
    global counter
    currBag = 'shiny gold'
    counter = sum(countChildren(currBag), 0)

    print(f'part 2: {counter}')


if __name__ == '__main__':
    main()
