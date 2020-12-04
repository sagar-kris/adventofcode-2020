
def main():
    # import data
    inp = open("./day2input.txt", 'r').read()
    # clean up data
    inp = inp.strip('\n')
    inp = inp.strip()
    inp = inp.split('\n')
    inp = [elem.strip() for elem in inp]

    validCount, validCount2 = 0, 0

    for entry in inp:
        # get useful data out
        elem = entry.split(' ')
        elem = [node.strip() for node in elem]
        nums = elem[0].split('-')
        lo, hi = int(nums[0]), int(nums[1])
        letter = elem[1].strip(':')
        pwd = elem[2]

        # PART 1
        if lo <= pwd.count(letter) <= hi:
            validCount += 1

        # PART 2
        lo -= 1
        hi -= 1
        if (pwd[lo] == letter or pwd[hi] == letter) and (pwd[lo] != pwd[hi]):
            validCount2 += 1

    print(f'part 1 valid passwords: {validCount}')
    print(f'part 2 valid passwords: {validCount2}')


if __name__ == '__main__':
    main()
