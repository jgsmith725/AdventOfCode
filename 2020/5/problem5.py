import os

def parseRow(row):
    ub = 127
    lb = 0
    for char in row:
        if char == "F":
            ub = ub - ((ub - lb + 1) / 2)
        elif char == "B":
            lb = lb + ((ub - lb + 1) / 2)
    return lb

def parseColumn(col):
    ub = 7
    lb = 0
    for char in col:
        if char == "L":
            ub = ub - ((ub - lb + 1) / 2)
        elif char == "R":
            lb = lb + ((ub - lb + 1) / 2)
    return lb

def getSeatID(row, column):
    return row * 8 + column

def part1(lines):
    highest_seat = 0
    for line in lines:
        rowstr = line[0:7]
        row = parseRow(rowstr)

        colstr = line[7:10]
        col = parseColumn(colstr)

        seat_id = getSeatID(row, col)
        if seat_id > highest_seat:
            highest_seat = seat_id

    print(highest_seat)

def part2(lines):
    seats = []
    for line in lines:
        rowstr = line[0:7]
        row = parseRow(rowstr)

        colstr = line[7:10]
        col = parseColumn(colstr)

        seat_id = getSeatID(row, col)
        seats.append(seat_id)
    
    seats.sort()
    for idx in range(1,len(seats)):
        if seats[idx - 1] + 2 == seats[idx]:
            print(str(seats[idx - 1]) + " " + str(seats[idx]))


def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    part1(lines)
    part2(lines)

if __name__== "__main__":
    main()