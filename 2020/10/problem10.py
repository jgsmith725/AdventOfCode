import os

def part1(lines):
    adapters = [0]
    for line in lines:
        val = int(line)
        adapters.append(val)
    adapters.sort()
    adapters.append(adapters[len(adapters) - 1] + 3)

    diffs1 = 0
    diffs3 = 0
    for idx in range(len(adapters)):
        if idx == 0:
            continue
        diff = adapters[idx] - adapters[idx - 1]
        if diff == 1:
            diffs1 = diffs1 + 1
        elif diff == 3:
            diffs3 = diffs3 + 1

    return diffs1 * diffs3

def traverse(adapters, idx, traverse_dict):
    if idx in traverse_dict:
        return traverse_dict[idx]
    if idx == len(adapters) - 1:
        return 1
    count = 0
    if idx + 1 < len(adapters) and adapters[idx + 1] - adapters[idx] <= 3:
        count = count + traverse(adapters, idx + 1, traverse_dict)
    if idx + 2 < len(adapters) and adapters[idx + 2] - adapters[idx] <= 3:
        count = count + traverse(adapters, idx + 2, traverse_dict)
    if idx + 3 < len(adapters) and adapters[idx + 3] - adapters[idx] <= 3:
        count = count + traverse(adapters, idx + 3, traverse_dict)

    traverse_dict[idx] = count
    return count

def part2(lines):
    adapters = [0]
    for line in lines:
        val = int(line)
        adapters.append(val)
    adapters.sort()
    adapters.append(adapters[len(adapters) - 1] + 3)

    return traverse(adapters, 0, {})
 


def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    #print(part1(lines))
    print(part2(lines))
    

if __name__== "__main__":
    main()