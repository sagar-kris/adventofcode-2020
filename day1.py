
def twoSum(inpList, targetSum):
    for elem in inpList:
        if targetSum-elem in inpList:
            return elem, targetSum - elem
    return None


def main():
    # import data
    inp = open("./day1input.txt", 'r').read()

    # clean up data
    inp = inp.strip('\n')
    inp = inp.strip()
    inp = inp.split('\n')
    inp = [int(elem.strip()) for elem in inp]

    # PART 1
    res1 = twoSum(inp, 2020)
    print(f'part 1: {res1[0]}, {res1[1]}. product = {res1[0] * res1[1]}')

    # PART 2
    for elemIdx2, elem2 in enumerate(inp):
        res2_1 = twoSum(inp[:elemIdx2] + inp[elemIdx2+1:], 2020-elem2)
        if res2_1:
            print(f'part 2: {res2_1[0]}, {res2_1[1]}, {elem2}. product = {res2_1[0] * res2_1[1] * elem2}')
            break


if __name__ == '__main__':
    main()
