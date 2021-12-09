import sys
sys.path.append('/Users/jack/Python/AdventOfCode/2019')
import helper
import intcode

def main(filename):
    inputArr = helper.getInputArr(filename, 0)
    arrCopy = inputArr.copy()
    output1 = intcode.getIntcodeOutput(arrCopy, 12, 2)
    print('part 1 = ' + str(output1))

    done = 0
    for input1 in range(0,100):
        for input2 in range(0,100):
            arrCopy = inputArr.copy()
            output = intcode.getIntcodeOutput(arrCopy, input1, input2)
            if output == 19690720:
                done = 1
                break
        if done == 1:
            break
    print('part 2 noun = ' + str(input1) + ' verb = ' + str(input2))

if __name__ == "__main__":
    main('Day2/day2input.txt')
    