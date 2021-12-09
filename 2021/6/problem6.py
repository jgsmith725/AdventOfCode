import os
import numpy as np
import math

def part1(lines, days):
    fish = np.array([int(string) for string in lines[0].split(",")])
    new_fish = np.array([])
    for day in range(days):
        zeros = np.size(fish) - np.count_nonzero(fish)
        fish = fish - 1
        new_fish = new_fish - 1
        fish = np.mod(fish, 7)
        newest_fish = np.full(zeros, 8)
        new_fish = np.append(new_fish, newest_fish)
        fish = np.append(fish, np.full(np.count_nonzero(new_fish == 6), 6))
        new_fish = new_fish[(new_fish > 6)]
        print("day " + str(day))
        print(np.append(fish, new_fish))

    print(len(fish) + len(new_fish))

def part2(lines, days):
    fish = np.array([int(string) for string in lines[0].split(",")])
    tot = 0
    ages = {}
    for age in range(9):
        ages[age] = np.count_nonzero(fish == age)

    for day in range(days):
        zeros = ages[0]
        
        for age in range(len(ages) - 1):
            ages[age] = ages[age+1]
        ages[8] = zeros
        ages[6] = ages[6] + zeros
    
    tot = 0
    for age in range(len(ages)):
        tot += ages[age]
    print(tot)
        
def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()
    days = 256


    #part1(lines, days)
    part2(lines, days)



if __name__== "__main__":
    main()