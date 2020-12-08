import os

def parseInput(line):
    instr = line.split(" ")[0]
    arg = line.split(" ")[1]
    return [instr, arg]

def part1(lines):
    acc = 0
    idx_dict = {}
    idx = 0
    while(True):
        if (idx in idx_dict):
            print("found: " + str(acc))
            break
        else:
            idx_dict[idx] = 1

        line = lines[idx].strip()
        [instr, arg] = parseInput(line)
        if instr == "nop":
            idx = idx + 1
            continue
        elif instr == "acc":
            acc = acc + int(arg)
            idx = idx + 1
        elif instr == "jmp":
            idx = idx + int(arg)
    return

def part2(lines):
    for search_idx in range(len(lines)):
        search_line = lines[search_idx]
        [search_instr, search_arg] = parseInput(search_line)
        if search_instr == "nop":
            lines[search_idx] = "jmp " + search_arg
        elif search_instr == "jmp":
            lines[search_idx] = "nop " + search_arg

        acc = 0
        idx_dict = {}
        idx = 0
        while(True):
            if idx == len(lines):
                print("found finite: " + str(acc))
                break
            if (idx in idx_dict):
                break
            else:
                idx_dict[idx] = 1

            line = lines[idx].strip()
            [instr, arg] = parseInput(line)
            if instr == "nop":
                idx = idx + 1
                continue
            elif instr == "acc":
                acc = acc + int(arg)
                idx = idx + 1
            elif instr == "jmp":
                idx = idx + int(arg)

        if search_instr == "nop":
            lines[search_idx] = "nop " + search_arg
        elif search_instr == "jmp":
            lines[search_idx] = "jmp " + search_arg
    return

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    print(part1(lines))
    print(part2(lines))
    

if __name__== "__main__":
    main()