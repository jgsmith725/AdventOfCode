import os

def parseInput(line):

    return []

def part1(lines):
    ansdict = {}
    groupcnt = 0
    for line in lines:
        if line == "\n":
            groupcnt = groupcnt + len(ansdict)
            ansdict = {}
        line = line.strip()
        for char in line:
            ansdict[char]=1
    return groupcnt

def part2(lines):
    ansdict = {}
    groupcnt = 0
    for line in lines:
        if line == "\n":
            count = 0
            for key in ansdict:
                if ansdict[key] == 1:
                    count = count + 1
            groupcnt = groupcnt + count
            ansdict = {}
            continue
        line = line.strip()
        if len(ansdict) == 0:
            for char in line:
                ansdict[char]=1
        else:
            for key in ansdict:
                if not key in line:
                    ansdict[key] = 0

    return groupcnt

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    print(part1(lines))
    print(part2(lines))
    

if __name__== "__main__":
    main()