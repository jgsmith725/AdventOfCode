import os

def part2(lines, preamble_length):
    done = False
    for start in range(0, len(lines)):
        if done: 
            break
        sum = int(lines[start])
        largest = int(lines[start])
        smallest = int(lines[start])
        for curr_idx in range(start+1, len(lines)):
            val = int(lines[curr_idx])
            sum = sum + val
            if val > largest:
                largest = val
            if val < smallest:
                smallest = val
            if sum == 90433990:
                print("smallest = " + str(smallest) + " largest = " + str(largest))
                print("tot = " + str(smallest + largest))
                done = True
                break
    

def part1(lines, preamble_length):
    for idx in range(preamble_length, len(lines)):
        valid = False
        for idx2 in range(idx-preamble_length, idx):
            if valid == True:
                break
            for idx3 in range(idx-preamble_length, idx):
                if idx2 == idx3:
                    continue
                if int(lines[idx2]) + int(lines[idx3]) == int(lines[idx]):
                    valid = True
                    break

        if valid == False:
            print(lines[idx])
            break 

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    #print(part1(lines, 25))
    print(part2(lines, 25))
    

if __name__== "__main__":
    main()