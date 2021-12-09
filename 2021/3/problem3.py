import os
import numpy as np
import math

def part1(lists):
    avgs = np.average(np.array(lists).astype(np.int32), axis=0)
    rounded = np.round(avgs, decimals=0)
    reversed = np.array(np.logical_not(np.array(rounded, dtype=np.bool8)), dtype=np.int32) #converts to boolean, reverses, and converts back to int
    bin = int("".join([str(math.trunc(int)) for int in rounded.tolist()]), 2)   #joins list into string, then converts to binary value
    bin_rev = int("".join([str(math.trunc(int)) for int in reversed.tolist()]), 2)
    print(bin * bin_rev)

def part2(lists):
    o2 = np.array(lists).astype(np.int32)
    co2 = o2
    avgs = np.average(o2, axis=0)
    rounded = np.round(avgs, decimals=0)
    reversed = np.array(np.logical_not(np.array(rounded, dtype=np.bool8)), dtype=np.int32) #converts to boolean, reverses, and converts back to int
    for col in range(len(lists[0])):
        o2 = o2[o2[:,col]==rounded[col]]
        avgs = np.average(o2, axis=0)
        rounded = np.floor(np.add(avgs, 0.5))
        if len(o2) < 2:
            break
    for col in range(len(reversed)):
        co2 = co2[co2[:,col]==reversed[col]]
        avgs = np.average(co2, axis=0)
        rounded = np.floor(np.add(avgs, 0.5))
        reversed = np.array(np.logical_not(np.array(rounded, dtype=np.bool8)), dtype=np.int32) #converts to boolean, reverses, and converts back to int
        if len(co2) < 2:
            break

    print(o2[0])
    bin_o2 = int("".join([str(math.trunc(int)) for int in o2[0].tolist()]), 2)   #joins list into string, then converts to binary value
    bin_co2 = int("".join([str(math.trunc(int)) for int in co2[0].tolist()]), 2)   #joins list into string, then converts to binary value
    print(bin_o2 * bin_co2)



def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()
    lists = []
    for line in lines:
        row = list(line.replace('\n', ''))
        lists.append(row)

    #part1(lists)
    part2(lists)



if __name__== "__main__":
    main()