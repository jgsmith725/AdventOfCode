import os

def part1(lines):
    limit = 999
    grid = [[0 for i in range(limit)]for j in range(limit)]
    for line in lines:
        p1 = [int(string) for string in line.split(" -> ")[0].split(",")]
        p2 = [int(string) for string in line.split(" -> ")[1].split(",")]

        if not (p1[0] == p2[0] or p1[1] == p2[1]):
            continue

        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
            for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                grid[x][y] += 1
    
    print(getDangerousAreas(grid))

def part2(lines):
    limit = 999
    grid = [[0 for i in range(limit)]for j in range(limit)]
    for line in lines:
        p1 = [int(string) for string in line.split(" -> ")[0].split(",")]
        p2 = [int(string) for string in line.split(" -> ")[1].split(",")]

        if p1[0] == p2[0] or p1[1] == p2[1]:
            for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                    grid[x][y] += 1
        else:
            xstep = 1 if p1[0] < p2[0] else -1
            ystep = 1 if p1[1] < p2[1] else -1
            y = p1[1]
            for x in range(p1[0], p2[0] + xstep, xstep):
                grid[x][y] += 1
                y += ystep
    
    print(getDangerousAreas(grid))

def getDangerousAreas(grid):
    dangerous = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] > 1:
                dangerous += 1
    return dangerous

        
def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    #part1(lines)
    part2(lines)



if __name__== "__main__":
    main()