import re

inp = 0


def cleanUp(inputFile):
    inputFile = inputFile.strip('\n')
    inputFile = inputFile.strip()
    inputFile = inputFile.split('\n\n')
    inputFile = [elem.strip() for elem in inputFile]
    inputFile = [elem.strip('\n') for elem in inputFile]
    inputFile = [elem.split(re.search(elem, ' \n')) for elem in inputFile]
    return inputFile


def validPassportP1(passport):
    validFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    validFieldsCount = 0

    for field in passport:
        if field[0:3] in validFields:
            validFieldsCount += 1
    if validFieldsCount == 7:
        return True
    return False


def validPassportP2(passport):
    validFieldsCount = 0

    # switcher = {
    #     'byr': lambda fieldStr: 1920 <= int(fieldStr[4:]) <= 2002,
    #     'iyr': lambda fieldStr: 2010 <= int(fieldStr[4:]) <= 2020,
    #     'eyr': lambda fieldStr: 2020 <= int(fieldStr[4:]) <= 2030,
    #     'hgt': lambda fieldStr: (fieldStr[-2:] == 'cm' and 150 <= int(fieldStr[4:-2]) <= 193) or (
    #             fieldStr[-2:] == 'in' and 59 <= int(fieldStr[4:-2]) <= 76),
    #     'hcl': lambda fieldStr: fieldStr[4] == '#' and len(fieldStr[5:]) == 6 and not [
    #         '0123456789abcdef'.find(char2) == -1 for char2 in fieldStr[5:]],
    #     'ecl': lambda fieldStr: fieldStr[4:] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    #     'pid': lambda fieldStr: len(fieldStr[4:]) == 9 and int(fieldStr[4:]) < 1000000000
    # }
    #
    # for field in passport:
    #     if switcher.get(field[0:3], lambda: False):
    #         validFieldsCount += 1
    # if validFieldsCount == 7:
    #     return True
    # return False

    for field in passport:
        if field[0:3] == 'byr':
            validFieldsCount += 1 if 1920 <= int(field[4:]) <= 2002 else 0
        elif field[0:3] == 'iyr':
            validFieldsCount += 1 if 2010 <= int(field[4:]) <= 2020 else 0
        elif field[0:3] == 'eyr':
            validFieldsCount += 1 if 2020 <= int(field[4:]) <= 2030 else 0
        elif field[0:3] == 'hgt':
            if field[-2:] == 'cm' and 150 <= int(field[4:-2]) <= 193:
                validFieldsCount += 1
            elif field[-2:] == 'in' and 59 <= int(field[4:-2]) <= 76:
                validFieldsCount += 1
        elif field[0:3] == 'hcl':
            if field[4] == '#' and len(field[5:]) == 6:
                tempCount = 0
                for char2 in field[5:]:
                    if '0123456789abcdef'.find(char2) != -1:
                        tempCount += 1
                if tempCount == 6:
                    validFieldsCount += 1
        elif field[0:3] == 'ecl':
            if field[4:] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                validFieldsCount += 1
        elif field[0:3] == 'pid':
            if len(field[4:]) == 9 and int(field[4:]) < 1000000000:
                validFieldsCount += 1

    if validFieldsCount == 7:
        return True
    return False


def main():
    global inp
    inp = open("./day4input.txt", 'r').read()
    inp = cleanUp(inp)  # result is array of formatted passports, each passport is array of fields

    # PART 1
    validPassportsCounterP1 = 0
    for passport in inp:
        if validPassportP1(passport):
            validPassportsCounterP1 += 1
    print(f'part 1: {validPassportsCounterP1}')

    # PART 2
    validPassportsCounterP2 = 0
    for passport in inp:
        if validPassportP1(passport) and validPassportP2(passport):
            validPassportsCounterP2 += 1
    print(f'part 2: {validPassportsCounterP2}')


if __name__ == '__main__':
    main()
