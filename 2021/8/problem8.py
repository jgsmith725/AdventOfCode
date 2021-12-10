import os
import numpy as np
import math

def part1(lines):
    #outputs = []
    ans = 0
    for line in lines:
        line = str(line).replace("\n", "")
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
        inputDict = getInputDict(line)   
        keyMap = {}
        keyMap[1] = inputDict[2][0]
        keyMap[7] = inputDict[3][0]
        keyMap[4] = inputDict[4][0]
        keyMap[8] = inputDict[7][0]

        chars = {}
        for input in inputDict[5]:
            for char in input:
                if not char in chars:
                    chars[char] = 1
                else:
                    chars[char] += 1
        
        for input in inputDict[5]:
            is3 = True
            for char in input:
                if chars[char] < 2:
                    is3 = False
                    break
            if is3:
                keyMap[3] = input
        
        for char in chars:
            if chars[char] == 1 and char in inputDict[4][0]:
                for input in inputDict[5]:
                    if keyMap[3] != input:
                        if char in input:
                            keyMap[5] = input
                        else:
                            keyMap[2] = input

        for input in inputDict[6]:
            for char in keyMap[1]:
                if char not in input:
                    keyMap[6] = input
                    
        
        for input in inputDict[6]:
            if input == keyMap[6]:
                continue
            for char in keyMap[4]:
                if char not in input:
                    keyMap[0] = input

        for input in inputDict[6]:
            if keyMap[0] != input and keyMap[6] != input:
                keyMap[9] = input
        

        numStr = ""
        outputs = line.split(" | ")[1].split(" ")
        for output in outputs:
            size = len(output)
            for input in inputDict[size]:
                found = True
                for char in output:
                    if char not in input:
                        found = False
                if found:
                    for key in keyMap:
                        if keyMap[key] == input:
                            numStr += str(key)
        ans += int(numStr)
    print(ans)

def getInputDict(line):
    inputDict = {}
    for input in line.split(" | ")[0].split(" "):
        size = len(input)
        if not size in inputDict:
            inputDict[size] = []
        if not input in inputDict[size]:
            inputDict[size].append(input)
    return inputDict

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()



    #part1(lines)
    part2(lines)



if __name__== "__main__":
    main()