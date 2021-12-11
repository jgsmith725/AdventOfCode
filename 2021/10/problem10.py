import os
import numpy as np
import statistics

def part1(lines):
    closers = []
    for line in lines:
        closer, stack = getIllegalCloser(line.replace("\n",""))
        if closer is not None:
            closers.append(closer)
    
    print(getTotalScore(closers))

def part2(lines):
    scores = []
    for line in lines:
        illegal, stack = getIllegalCloser(line.replace("\n",""))
        if illegal is None:
            remainingStack = getRemainingStack(stack)
            score = getStackScore(remainingStack)
            scores.append(score)

    print(statistics.median(scores))

def getRemainingStack(stack):
    remainingStack = []
    while len(stack) > 0:
        complement = getComplement(stack.pop())
        remainingStack.append(complement)
    return remainingStack


def getStackScore(stack):
    tot = 0
    for char in stack:
        tot = tot * 5
        tot = tot + getCloserScore(char)
    return tot

def getCloserScore(closer):
    if closer == ")":
        return 1
    elif closer == "]":
        return 2
    elif closer == "}":
        return 3
    elif closer == ">":
        return 4
    return None

def getIllegalCloser(line):
    stack = []
    for char in line:
        if char in "([{<":
            stack.append(char)
        else:
            complement = getComplement(char)
            if stack.pop() != complement:
                return char, stack

    return None, stack
    

def getComplement(char):
    if char == ")":
        return "("
    elif char == "]":
        return "["
    elif char == "}":
        return "{"
    elif char == ">":
        return "<"
    elif char == "(":
        return ")"
    elif char == "[":
        return "]"
    elif char == "{":
        return "}"
    elif char == "<":
        return ">"
    return None

def getTotalScore(illegalClosers):
    tot = 0
    for closer in illegalClosers:
        if closer == ")":
            tot += 3
        elif closer == "]":
            tot += 57
        elif closer == "}":
            tot += 1197
        elif closer == ">":
            tot += 25137
    return tot
    

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()



    #part1(lines)
    part2(lines)



if __name__== "__main__":
    main()
