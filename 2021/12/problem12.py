import os
from enum import Enum

class Size(Enum):
    SMALL = 1
    LARGE = 2


class Cave:
    def __init__(self, name, connections):
        self.name = str(name)
        self.size = Size.LARGE if str(name).isupper() else Size.SMALL
        self.connections = connections

def parseInput(lines):
    caves = {}
    for line in lines:
        cave0 = line.replace("\n","").split("-")[0]
        cave1 = line.replace("\n","").split("-")[1]
        if not cave0 in caves:
            caves[cave0] = Cave(cave0, [cave1])
        elif not cave1 in caves[cave0].connections:
            caves[cave0].connections.append(cave1)

        if not cave1 in caves:
            caves[cave1] = Cave(cave1, [cave0])
        elif not cave0 in caves[cave1].connections:
            caves[cave1].connections.append(cave0)
    return caves

def findPaths(caves):
    path = []
    cave = caves["start"]
    path_count = traverse(caves, cave, path)
    return path_count

def traverse(caves: dict, cave: Cave, path: list):
    if cave.size == Size.SMALL and cave.name in path:
        return 0

    path.append(cave.name)

    if cave.name == "end":
        print(",".join(path))
        return 1

    path_count = 0
    for new_cave_name in cave.connections:
        path_count += traverse(caves, caves[new_cave_name], path.copy())
    return path_count

def findPaths2(caves):
    path = []
    cave = caves["start"]
    path_count = traverse2(caves, cave, path, False)
    return path_count

def traverse2(caves: dict, cave: Cave, path: list, used_extra_visit: bool):
    if cave.size == Size.SMALL and cave.name in path:
        if used_extra_visit or cave.name == "start" or cave.name == "end":
            return 0
        else:
            used_extra_visit = True

    path.append(cave.name)

    if cave.name == "end":
        print(",".join(path))
        return 1

    path_count = 0
    for new_cave_name in cave.connections:
        path_count += traverse2(caves, caves[new_cave_name], path.copy(), used_extra_visit)
    return path_count

def part1(lines):
    caves = parseInput(lines)
    print(findPaths(caves))


def part2(lines):
    caves = parseInput(lines)
    print(findPaths2(caves))

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    #part1(lines)
    part2(lines)



if __name__== "__main__":
    main()
