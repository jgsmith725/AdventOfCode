import os

def parseInput(line):

    return []

def part1(lines):
    for line in lines:
    return

def part2(lines):
    for line in lines:
    return

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    print(part1(lines))
    print(part2(lines))
    

if __name__== "__main__":
    main()