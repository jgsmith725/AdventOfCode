import os
import numpy as np
import math

def part1(lines):
    #outputs = []
    ans = 0
    for line in lines:
        line = str(line).replace("\n", "")
        input = line.split(" | ")[0]
        output = line.split(" | ")[1]
        outputs = output.split(" ")
        for num in outputs:
            size = len(num)
            if size == 2 or size == 3 or size == 4 or size == 7:
                ans += 1
        #outputs.append(output)

    print(ans)
    
def part2(lines):
    #outputs = []
    ans = 0
    for line in lines:
        line = str(line).replace("\n", "")
        input = line.split(" | ")[0]
        

        output = line.split(" | ")[1]
        outputs = output.split(" ")
        for num in outputs:
            size = len(num)
            if size == 2 or size == 3 or size == 4 or size == 7:
                ans += 1
        #outputs.append(output)

    print(ans)


def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()



    #part1(lines)
    part2(lines)



if __name__== "__main__":
    main()