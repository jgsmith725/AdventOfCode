import sys
sys.path.append('/Users/jack/Python/AdventOfCode/2019')
import helper

def calcFuelRequired(mass, total = 0):
    amtRequired = int(mass / 3) - 2
    if int(amtRequired) < 1:
        return total
    else:
        total += amtRequired
        return calcFuelRequired(amtRequired, total)


def main(filename):
    modules = helper.getInputArr(filename)
    totalRequired = 0
    for module in modules:
         totalRequired += calcFuelRequired(module)
    print(totalRequired)

if __name__ == "__main__":
    main('Day1/day1input.txt')
    