import os

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()
    hpos = 0
    depth = 0
    aim = 0
    for line in lines:
        dir = line.split(" ")[0]
        val = int(line.split(" ")[1])
        if dir == "forward":
            hpos += val
            depth = depth + aim * val
        elif dir == "up":
            aim -= val
        elif dir == "down":
            aim += val

    print(hpos * depth)

if __name__== "__main__":
    main()