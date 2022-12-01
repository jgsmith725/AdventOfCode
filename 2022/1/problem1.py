import os

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()
    elves = []
    elf = 0
    for line in lines:
        if line is '\n':
            elves.append(elf)
            elf = 0
        else:
            elf += int(line)

    if elf > 0:
        elves.append(elf)

    topElf = max(elves)
    elves.pop(elves.index(topElf))
    twoElf = max(elves)
    elves.pop(elves.index(twoElf))
    threeElf = max(elves)
    elves.pop(elves.index(threeElf))

    print(topElf + twoElf + threeElf)

if __name__== "__main__":
    main()