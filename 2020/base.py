import os

def parseInput(line):

    return []

def part1(lines):
    for line in lines:
        [] =parseInput(line)
    return

def part2(lines):
    for line in lines:
        [] = parseInput(line)
    return

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    part1(lines)
    part2(lines)
    

if __name__== "__main__":
    main()