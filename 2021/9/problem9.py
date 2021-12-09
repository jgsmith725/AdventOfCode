import os
import numpy as np
import math

def part1(lines):
    grid = []
    for line in lines:
        row = [int(string) for string in list(line.split('\n')[0])]
        grid.append(row)
    
    low_points = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if isLowest(grid, x, y):
                low_points.append(grid[y][x])
    print(sum(low_points) + len(low_points))

def isLowest(grid, x, y):
    val = grid[y][x]
    if x != 0 and grid[y][x-1] <= val:
        return False
    if x != len(grid[y]) - 1 and grid[y][x+1] <= val:
        return False
    if y != 0 and grid[y-1][x] <= val:
        return False
    if y != len(grid) - 1 and grid[y+1][x] <= val:
        return False
    return True

def part2(lines):
    grid = []
    searched = []
    for line in lines:
        row = [int(string) for string in list(line.split('\n')[0])]
        grid.append(row)
        searched.append([0 for i in range(len(row))])
    
    basins = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            basin = getBasinSize(grid, x, y, searched, 0)
            if basin == 0:
                continue
            basins.append(basin)
            #print(basin)
    
    max1 = max(basins)
    print(max1)
    basins.pop(basins.index(max1))
    max2 = max(basins)
    print(max2)
    basins.pop(basins.index(max2))
    max3 = max(basins)
    print(max3)
    basins.pop(basins.index(max3))

    print(max1 * max2 * max3)


def getBasinSize(grid, x, y, searched, size):
    if y < 0 or y == len(grid):
        return 0
    if x < 0 or x == len(grid[y]):
        return 0
    if grid[y][x] == 9:
        return 0
    if searched[y][x] == 1:
        return 0
    
    size += 1
    searched[y][x] = 1
    size += getBasinSize(grid, x - 1, y, searched, 0)
    size += getBasinSize(grid, x + 1, y, searched, 0)
    size += getBasinSize(grid, x, y - 1, searched, 0)
    size += getBasinSize(grid, x, y + 1, searched, 0)
    return size
    


#def part2(lines):

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()



    #part1(lines)
    part2(lines)



if __name__== "__main__":
    main()