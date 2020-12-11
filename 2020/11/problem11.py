import os

def move(grid, visible):
    new_grid = []
    change = False
    for y in range(len(grid)):
        new_row = []
        for x in range(len(grid[y])):
            val = grid[y][x]
            if val == ".":
                new_row.append(".")
            else:
                if visible:
                    [empty_count, occ_count, floor_count] = getAdjacentVisible(grid, y, x)
                else:
                    [empty_count, occ_count, floor_count] = getAdjacent(grid, y, x)
                if val == "L":
                    if occ_count == 0:
                        new_row.append("#")
                        change = True
                    else:
                        new_row.append("L")
                elif val == "#":
                    if visible and occ_count >= 5:
                        change = True
                        new_row.append("L")
                    elif not visible and occ_count >= 4:
                        change = True
                        new_row.append("L")
                    else:
                        new_row.append("#")
                else:
                    new_row.append(".")
        new_grid.append(new_row)
    return [change, new_grid]

def getOccupiedTotal(grid):
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "#":
                count = count + 1
    return count

def getAdjacentVisible(grid, y, x):
    empty_count = 0
    occ_count = 0
    floor_count = 0

    [empty_count, occ_count, floor_count] = getCountsInDir(grid, y, x, -1, -1, empty_count, occ_count, floor_count)
    [empty_count, occ_count, floor_count] = getCountsInDir(grid, y, x, 0, -1, empty_count, occ_count, floor_count)
    [empty_count, occ_count, floor_count] = getCountsInDir(grid, y, x, 1, -1, empty_count, occ_count, floor_count)
    [empty_count, occ_count, floor_count] = getCountsInDir(grid, y, x, -1, 0, empty_count, occ_count, floor_count)
    [empty_count, occ_count, floor_count] = getCountsInDir(grid, y, x, 1, 0, empty_count, occ_count, floor_count)
    [empty_count, occ_count, floor_count] = getCountsInDir(grid, y, x, -1, 1, empty_count, occ_count, floor_count)
    [empty_count, occ_count, floor_count] = getCountsInDir(grid, y, x, 0, 1, empty_count, occ_count, floor_count)
    [empty_count, occ_count, floor_count] = getCountsInDir(grid, y, x, 1, 1, empty_count, occ_count, floor_count)

    return [empty_count, occ_count, floor_count]

def getCountsInDir(grid, y, x, y_dir, x_dir, empty_count, occ_count, floor_count):
    count = 1
    while True:
        y_coord = y + count * y_dir
        x_coord = x + count * x_dir
        if isInBounds(grid, y_coord, x_coord):
            val = grid[y_coord][x_coord]
            if val == ".":
                count = count + 1
                continue
            [empty_count, occ_count, floor_count] = incrementCount(val, empty_count, occ_count, floor_count)
            break
        else:
            break
    return [empty_count, occ_count, floor_count]

def getAdjacent(grid, y, x):
    empty_count = 0
    occ_count = 0
    floor_count = 0
    if isInBounds(grid, y-1, x-1):
        val = grid[y-1][x-1] 
        [empty_count, occ_count, floor_count] = incrementCount(val, empty_count, occ_count, floor_count)
    if isInBounds(grid, y, x-1):
        val = grid[y][x-1] 
        [empty_count, occ_count, floor_count] = incrementCount(val, empty_count, occ_count, floor_count)
    if isInBounds(grid, y+1, x-1):
        val = grid[y+1][x-1] 
        [empty_count, occ_count, floor_count] = incrementCount(val, empty_count, occ_count, floor_count)
    if isInBounds(grid, y-1, x):
        val = grid[y-1][x] 
        [empty_count, occ_count, floor_count] = incrementCount(val, empty_count, occ_count, floor_count)
    if isInBounds(grid, y+1, x):
        val = grid[y+1][x] 
        [empty_count, occ_count, floor_count] = incrementCount(val, empty_count, occ_count, floor_count)
    if isInBounds(grid, y-1, x+1):
        val = grid[y-1][x+1] 
        [empty_count, occ_count, floor_count] = incrementCount(val, empty_count, occ_count, floor_count)
    if isInBounds(grid, y, x+1):
        val = grid[y][x+1] 
        [empty_count, occ_count, floor_count] = incrementCount(val, empty_count, occ_count, floor_count)
    if isInBounds(grid, y+1, x+1):
        val = grid[y+1][x+1] 
        [empty_count, occ_count, floor_count] = incrementCount(val, empty_count, occ_count, floor_count)
    return [empty_count, occ_count, floor_count]

    
def incrementCount(val, empty_count, occ_count, floor_count):
    if val == "L":
        empty_count = empty_count + 1
    elif val == "#":
        occ_count = occ_count + 1
    else:
        floor_count = floor_count + 1
    
    return [empty_count, occ_count, floor_count]

def isInBounds(grid, y, x):
    return  y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])


def part2(lines):
    grid = []
    for line in lines:
        line = line.strip()
        row = []
        for char in line:
            row.append(char)
        grid.append(row)
    
    while(True):
        [change, grid] = move(grid, True)
        if not change:
            break
    

    return getOccupiedTotal(grid)


def part1(lines):
    grid = []
    for line in lines:
        line = line.strip()
        row = []
        for char in line:
            row.append(char)
        grid.append(row)
    
    while(True):
        [change, grid] = move(grid, False)
        if not change:
            break
    
    return getOccupiedTotal(grid)


def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    print(part1(lines))
    print(part2(lines))
    

if __name__== "__main__":
    main()