import os

def part2(lines):
    buses = []
    offsets = []
    arr = lines[0].strip().split(",")
    for idx in range(len(arr)):
        val = arr[idx]
        if not val == "x":
            buses.append(int(val))
            offsets.append(idx)
    
    time = 1
    idxs_to_check = 1
    time_jump = 1
    while True:
        valid = True
        lcm = 1
        for idx in range(idxs_to_check):
            bus = buses[idx]
            offset = offsets[idx]
            lcm = lcm * bus
            if (time + offset) % bus != 0:
                valid = False
                break
        if valid == True:
            if idxs_to_check == len(buses):
                break
            idxs_to_check = idxs_to_check + 1
            time_jump = lcm
        time = time + time_jump

    return time

def part1(input, lines):
    buses = []
    arr = lines[0].strip().split(",")  
    for val in arr:
        if not val == "x":
            buses.append(int(val))
    
    done = False
    time = input
    while True:
        for bus in buses:
            if time % bus == 0:
                done = True
                break
        if done == True:
            break
        time = time + 1

    return bus * (time - input)

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    #print(part1(939, lines))
    #print(part1(1000390, lines))
    print(part2(lines))
    

if __name__== "__main__":
    main()