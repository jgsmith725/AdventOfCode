import os
import numpy as np

lowest_score = 9999999999999

def parseInput(lines):
    grid = []
    for line in lines:
        row = []
        for char in line.replace("\n", ""):
            row.append(int(char))
        grid.append(row)
    return grid

def part1(lines):
    grid = parseInput(lines)
    path = []
    loc = (0, 0)
    traverse(grid, loc, path)

def isValidLoc(loc, grid):
    return loc[0] >= 0 and loc[0] < len(grid) and loc[1] >= 0 and loc[1] < len(grid[0])


def isEndLoc(loc, grid):
    return loc[0] == len(grid) - 1 and loc[1] == len(grid[0]) - 1

def getRiskAtLoc(loc, grid):
    return grid[loc[0]][loc[1]]

def getRiskTot(path, grid, show = False):
    risk_tot = 0
    for loc in path:
        risk_tot += getRiskAtLoc(loc, grid)
        if show:
            print("at loc " + str(loc) + " score: " + str(risk_tot))
    return risk_tot


def traverse(grid, loc, path: list):
    global lowest_score
    if not isValidLoc(loc, grid) or loc in path or getRiskTot(path, grid) > lowest_score:
        return

    path.append(loc)
    #print('appended' + str(loc))
    
    if isEndLoc(loc, grid):
        risk_tot = getRiskTot(path, grid, False)
        if risk_tot < lowest_score:
            lowest_score = risk_tot
            print(path)
            print(risk_tot)
        return lowest_score
 
    traverse(grid, (loc[0] + 1, loc[1]), path.copy())
    traverse(grid, (loc[0], loc[1] + 1), path.copy())
    traverse(grid, (loc[0] - 1, loc[1]), path.copy())
    traverse(grid, (loc[0], loc[1] - 1), path.copy())
    
    

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    part1(lines)
    #part2(grid)



if __name__== "__main__":
    main()
