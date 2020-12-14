import os

class FloatingMask():
    def __init__(self, positions_0, positions_1):
        self.and_mask = 2**36 - 1
        self.or_mask = 0
        initMasks(positions_0, positions_1)

    def initMasks(positions_0, positions_1):
        for pos in positions_0:
            and_mask = and_mask - (2 ** (35 - pos))
        for pos in positions_1:
            or_mask = or_mask + (2 ** (35 - pos))

def getFloatingMasks(floating_positions):
    floating_masks = []
    for pos in floating_positions:
        #need to figure out how to get every combo

def part2(lines):
    mem_dict = {}
    for line in lines:
        line = line.strip()
        if line.split(" = ")[0] == "mask":
            mask_str = line.split(" = ")[1]
            or_mask = 0
            and_mask = 2**36 - 1
            floating_masks = []
            floating_positions = []
            for pos in range(len(mask_str) - 1, -1, -1):
                #mask of 0s specify 1s OR value
                if mask_str[pos] == "1":
                    or_mask = or_mask + (2 ** (35 - pos))
                #mask of 1s specify 0s AND value
                elif mask_str[pos] == "X":
                    floating_positions.append(pos)
            floating_masks = getFloatingMasks(floating_positions)
                    
        else:
            addr = int(line.split("[")[1].split("]")[0])
            val = int(line.split(" = ")[1])
            val = val | or_mask
            val = val & and_mask
            mem_dict[addr] = int(val)

    tot = 0
    for addr in mem_dict:
        tot = tot + mem_dict[addr]
            
    return tot

def part1(lines):
    mem_dict = {}
    for line in lines:
        line = line.strip()
        if line.split(" = ")[0] == "mask":
            mask_str = line.split(" = ")[1]
            or_mask = 0
            and_mask = 2**36 - 1
            for pos in range(len(mask_str) - 1, -1, -1):
                #mask of 0s specify 1s OR value
                if mask_str[pos] == "1":
                    or_mask = or_mask + (2 ** (35 - pos))
                #mask of 1s specify 0s AND value
                elif mask_str[pos] == "0":
                    and_mask = and_mask - (2 ** (35 - pos))
        else:
            addr = int(line.split("[")[1].split("]")[0])
            val = int(line.split(" = ")[1])
            val = val | or_mask
            val = val & and_mask
            mem_dict[addr] = int(val)

    tot = 0
    for addr in mem_dict:
        tot = tot + mem_dict[addr]
            
    return tot

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    print(part1(lines))
    print(part2(lines))
    

if __name__== "__main__":
    main()