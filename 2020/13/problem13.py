import os

def part2(lines):
    buses = []
    offsets = []
    arr = lines[0].strip().split(",")
    biggest = 0
    biggest_offset = 0
    time_start = 1  
    for idx in range(len(arr)):
        val = arr[idx]
        if not val == "x":
            time_start = time_start * int(val)
            if int(val) > biggest:
                biggest = int(val)
                biggest_offset = idx
            buses.append(int(val))
            offsets.append(idx)
    
    time = time_start - biggest_offset
    while True:
        valid = True
        for idx in range(len(buses)):
            bus = buses[idx]
            offset = offsets[idx]
            if (time + offset) % bus != 0:
                valid = False
                break
        if valid == True:
            break
        time = time - biggest

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