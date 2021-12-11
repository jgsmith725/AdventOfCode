import os

def part1(lines, steps):
    grid = []
    flashCount = 0
    for line in lines:
        row = [int(string) for string in line.replace("\n", "")]
        grid.append(row)

    for step in range(steps):
        grid, flashCount = doStep(grid, flashCount)
    print(flashCount)

def part2(lines):
    grid = []
    flashCount = 0
    for line in lines:
        row = [int(string) for string in line.replace("\n", "")]
        grid.append(row)

    step = 0
    while True:
        originalFlashCount = flashCount
        grid, flashCount = doStep(grid, flashCount)
        step = step + 1
        print(step)
        if originalFlashCount + len(grid) * len(grid[0]) == flashCount:
            print("synchronized at step " + str(step))
            break




def doStep(grid, flashCount):
    for row in range(len(grid)):
        for octopus in range(len(grid[row])):
            grid[row][octopus] += 1
    flashCount = flash(grid, flashCount)
    grid = resetGrid(grid)
    return grid, flashCount

def flash(grid, flashCount):
    flashLocs = []
    for row in range(len(grid)):
        for octopus in range(len(grid[row])):
            if grid[row][octopus] > 9:
                flashLocs.append((row, octopus))

    flashCount = chainFlash(grid, flashLocs, flashCount)
    return flashCount

def chainFlash(grid, flashLocs, flashCount):
    flashCount += len(flashLocs)
    while len(flashLocs) > 0:
        newLocs = []
        for loc in flashLocs:
            newLocs = newLocs + flashNeighbors(grid, loc[0], loc[1])
        flashCount += len(newLocs)
        flashLocs = newLocs
    return flashCount


    
def flashNeighbors(grid, row, octopus):
    flashLocs = []
    flashLocs = flashAtLoc(grid, row, octopus + 1, flashLocs)
    flashLocs = flashAtLoc(grid, row, octopus - 1, flashLocs)
    flashLocs = flashAtLoc(grid, row + 1, octopus, flashLocs)
    flashLocs = flashAtLoc(grid, row - 1, octopus, flashLocs)
    flashLocs = flashAtLoc(grid, row + 1, octopus + 1, flashLocs)
    flashLocs = flashAtLoc(grid, row + 1, octopus - 1, flashLocs)
    flashLocs = flashAtLoc(grid, row - 1, octopus + 1, flashLocs)
    flashLocs = flashAtLoc(grid, row - 1, octopus - 1, flashLocs)
    return flashLocs

def flashAtLoc(grid, row, octopus, flashLocs):
    if isValid(grid, row, octopus):
        grid[row][octopus] += 1
        if grid[row][octopus] == 10:
            flashLocs.append((row, octopus))
    return flashLocs

def isValid(grid, row, octopus):
    return row >= 0 and row < len(grid) and octopus >= 0 and octopus < len(grid[row])

def resetGrid(grid):
    for row in range(len(grid)):
        for octopus in range(len(grid[row])):
            if grid[row][octopus] > 9:
                grid[row][octopus] = 0
    return grid

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    #part1(lines, 100)
    part2(lines)



if __name__== "__main__":
    main()
