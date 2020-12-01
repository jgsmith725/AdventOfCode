import os
import math
import numpy as np
import time

grid_size = 300
serial_num = 7139

def main():
    first = True
    for x in range (0, grid_size):
        col = [] 
        for y in range(0,grid_size):
            col.append(getPowerLevel(x+1, y+1, serial_num))
        if first:
            grid = np.array([col])
            first = False
        else:
            grid = np.append(grid, [col], axis=0)

    t0 = time.time()
    max_power = 0
    for x in range (0, grid_size):
        for y in range(0, grid_size):
            max_size = min(grid_size - x, grid_size - y) + 1
            for size in range(1, max_size):
                print('current = ' + str(x) + ' ' + str(y) + ' ' + str(size))
                power = getAreaPowerNP(x, y, size, grid)
                if power > max_power:
                    max_power = power
                    max_power_loc = [x+1, y+1, size]
    t1 = time.time()
    print('max power loc = ' + str(max_power_loc))
    print('time = ' + str(t1 - t0))

def getPowerLevel(x, y, serial_num):
    rack_id = x+10
    power_level = rack_id * y
    power_level = power_level + serial_num
    power_level = power_level * rack_id
    hundreds_digit = int((power_level % 1000) / 100)
    return hundreds_digit - 5

def getAreaPowerNP(x_start, y_start, size, grid):
    return np.sum(grid[x_start:x_start + size, y_start:y_start+size])

def getAreaPower(x_start, y_start, size, grid):
    tot_power = 0
    for x in range(x_start, x_start+size):
        for y in range(y_start, y_start+size):
            tot_power = tot_power + grid[x][y]
    return tot_power

if __name__== "__main__":
    main()