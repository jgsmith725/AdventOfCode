import os
import numpy as np
import math

def part1(lines):
    positions = [int(string) for string in lines[0].split(",")]
    a = np.array(positions)
    closest = None
    closest_tot = None
    for pos in range(max(positions)+1):
        tot = np.sum(abs(a - pos))
        if closest is None or tot < closest_tot:
            closest = pos
            closest_tot = tot
    print(closest)
    print(closest_tot)

def part2(lines):
    positions = [int(string) for string in lines[0].split(",")]
    a = np.array(positions)
    closest = None
    closest_tot = None
    for pos in range(max(positions)+1):
        move = abs(a - pos)
        diff = np.add(np.divide(move, 2), 0.5)

        move = np.multiply(move, diff)
        tot = np.sum(move)
        if closest is None or tot < closest_tot:
            closest = pos
            closest_tot = tot
    print(closest)
    print(closest_tot)
        
def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()



    part1(lines)
    #part2(lines, days)



if __name__== "__main__":
    main()