import os
import numpy as np

def parseInput(lines):
    biggest_col = 0
    biggest_row = 0
    points = []
    folds = []
    parsingFolds = False
    for line in lines:
        if line == "\n":
            parsingFolds = True
            continue
        
        if not parsingFolds:
            col = int(line.split(",")[0])
            row = int(line.replace("\n","").split(",")[1])

            biggest_col = max(biggest_col, col)
            biggest_row = max(biggest_row, row)

            points.append((row, col))
            
        else:
            axis = line.split(" ")[2].split("=")[0]
            loc = int(line.split(" ")[2].split("=")[1])
            folds.append((axis, loc))
        
    grid = [["." for j in range(biggest_col + 1)] for i in range(biggest_row + 1)]
    for point in points:
        grid[point[0]][point[1]] = "#"
    return grid, folds

def fold(grid, fold):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "#":
                folded_row, folded_col = getInverse(row, col, fold)
                if folded_row is not None:
                    grid[folded_row][folded_col] = "#"
                    grid[row][col] = "."
    
    return grid


def getInverse(row, col, fold):
    fold_loc = fold[1]
    if fold[0] == "x" and col > fold_loc:
        return row, fold_loc - abs(col - fold_loc)
    elif fold[0] == "y" and row > fold_loc: 
        return fold_loc - abs(row - fold_loc), col
    return None, None

def countPoints(grid):
    return np.count_nonzero(np.array(grid) == "#")

def resize(grid, rows, cols, start_col):
    new_grid = [["." for j in range(cols + 1)] for i in range(rows + 1)]
    for row in range(len(grid)):
        for col in range(start_col, len(grid[row])):
            if grid[row][col] == "#":
                new_grid[row][col - start_col] = "#"
    return new_grid

def part1(lines):
    grid, folds = parseInput(lines)
    grid = fold(grid, folds[0])
    print(countPoints(grid))

def part2(lines):
    grid, folds = parseInput(lines)
    for _fold in folds:
        grid = fold(grid, _fold)

    grid = resize(grid, 5, 40, 0)
    print(grid)

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    part1(lines)
    #part2(lines)



if __name__== "__main__":
    main()
