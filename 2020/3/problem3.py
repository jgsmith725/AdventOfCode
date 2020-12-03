import os
def parseInput(lines):
    return []

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()
    x = 0
    trees = 0
    width = len(lines[0].split("\n")[0])
    cnt = 0
    for line in lines:
        if cnt % 2 == 1:
            cnt = cnt + 1
            continue
        if line[x] == "#":
            trees = trees + 1
        x = x + 1
        x = x % width
        cnt = cnt + 1
    
    print(trees)

if __name__== "__main__":
    main()