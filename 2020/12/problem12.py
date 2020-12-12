import os

def parseInput2(line, pos_x, pos_y, wp_x, wp_y):
    line = line.strip()
    if line[0] == "N":
        wp_y = wp_y + int(line[1:])
    if line[0] == "S":
        wp_y = wp_y - int(line[1:])
    if line[0] == "E":
        wp_x = wp_x + int(line[1:])
    if line[0] == "W":
        wp_x = wp_x - int(line[1:])
    if line[0] == "L" or line[0] == "R":
        rotations = int(line[1:])
        [wp_x, wp_y] = rotate(rotations, line[0], wp_x, wp_y)
    if line[0] == "F":
            pos_y = pos_y + wp_y * int(line[1:])
            pos_x = pos_x + wp_x * int(line[1:])

    return [pos_x, pos_y, wp_x, wp_y]

def rotate(rotation, dir, wp_x, wp_y):
    temp_x = wp_x
    temp_y = wp_y
    if (dir == "R" and rotation == 90) or (dir == "L" and rotation == 270):
        wp_y = -wp_x
        wp_x = temp_y
    if rotation == 180:
        wp_y = -wp_y
        wp_x = -wp_x
    if (dir == "R" and rotation == 270) or (dir == "L" and rotation == 90):
        wp_y = wp_x
        wp_x = -temp_y
    return [wp_x, wp_y]

def parseInput(line, pos_x, pos_y, dir):
    line = line.strip()
    if line[0] == "N":
        pos_y = pos_y + int(line[1:])
    if line[0] == "S":
        pos_y = pos_y - int(line[1:])
    if line[0] == "E":
        pos_x = pos_x + int(line[1:])
    if line[0] == "W":
        pos_x = pos_x - int(line[1:])
    if line[0] == "L":
        rotations = int(line[1:])/90
        dir = (dir + rotations) % 4
    if line[0] == "R":
        rotations = int(line[1:])/90
        dir = (dir - rotations) % 4
    if line[0] == "F":
        if dir == 1:
            pos_y = pos_y + int(line[1:])
        if dir == 3:
            pos_y = pos_y - int(line[1:])
        if dir == 0:
            pos_x = pos_x + int(line[1:])
        if dir == 2:
            pos_x = pos_x - int(line[1:])

    return [pos_x, pos_y, dir]



def part1(lines):
    dir = 0
    pos_x = 0
    pos_y = 0
    for line in lines:
        [pos_x, pos_y, dir] = parseInput(line, pos_x, pos_y, dir)
    return abs(pos_x) + abs(pos_y)

def part2(lines):
    dir = 0
    pos_x = 0
    pos_y = 0
    wp_x = 10
    wp_y = 1
    for line in lines:
        [pos_x, pos_y, wp_x, wp_y] = parseInput2(line, pos_x, pos_y, wp_x, wp_y)
    return abs(pos_x) + abs(pos_y)

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    print(part1(lines))
    print(part2(lines))
    

if __name__== "__main__":
    main()