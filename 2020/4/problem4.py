import os

def parseInput(lines):
    return []

def isCharValid(char):
    if char == "0":
        return True
    if char == "1":
        return True
    if char == "2":
        return True
    if char == "3":
        return True
    if char == "4":
        return True
    if char == "5":
        return True
    if char == "6":
        return True
    if char == "7":
        return True
    if char == "8":
        return True
    if char == "9":
        return True
    if char == "a":
        return True
    if char == "b":
        return True
    if char == "c":
        return True
    if char == "d":
        return True                                                                        
    if char == "e":
        return True
    if char == "f":
        return True                
    return False

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()
    found = 0
    valid = 0

    for line in lines:
        if line == "\n":
            if found >= 7:
                valid = valid + 1
            found = 0
            continue
        line = line.strip()
        if len(line.split("byr:")) > 1:
            val = int(line.split("byr:")[1].split(" ")[0])
            if (val >= 1920 and val <= 2002):
                found = found + 1
        if len(line.split("iyr:")) > 1:
            val = int(line.split("iyr:")[1].split(" ")[0])
            if val >= 2010 and val <= 2020:
                found = found + 1
        if len(line.split("eyr:")) > 1:
            val = int(line.split("eyr:")[1].split(" ")[0])
            if val >= 2020 and val <= 2030:
                found = found + 1
        if len(line.split("hgt:")) > 1:
            val = line.split("hgt:")[1].split(" ")[0]
            if len(val.split("cm")) > 1:
                if int(val.split("cm")[0]) >= 150 and int(val.split("cm")[0]) <= 193:
                    found = found + 1
            elif len(val.split("in")) > 1:
                if int(val.split("in")[0]) >= 59 and int(val.split("in")[0]) <= 76:
                    found = found + 1
        if len(line.split("hcl:")) > 1:
            val = line.split("hcl:")[1].split(" ")[0]
            if len(val) == 7 and val[0] == "#":
                invalid = False
                for idx in range(1, len(val)):
                    if not isCharValid(val[idx]):
                        invalid = True
                        break
                if not invalid:
                    found = found + 1
        if len(line.split("ecl:")) > 1:
            val = line.split("ecl:")[1].split(" ")[0]
            if val == "amb" or val == "blu" or val == "brn" or val == "gry" or val == "grn" or val == "hzl" or val == "oth":
                found = found + 1
        if len(line.split("pid:")) > 1:
            val = line.split("pid:")[1].split(" ")[0]
            if len(val) == 9:
                invalid = False
                for char in val:
                    if not(char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9"):
                        invalid = True
                if not invalid:
                    found = found + 1
    print(valid)
if __name__== "__main__":
    main()