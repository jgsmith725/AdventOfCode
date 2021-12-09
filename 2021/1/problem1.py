import os

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()
    prev1 = 999999999999
    prev2 = 999999999999
    prev3 = 999999999999
    increases = 0
    for line in lines:
        if int(line) > prev3:
            increases += 1
        prev3 = prev2
        prev2 = prev1
        prev1 = int(line)

    print(increases)

if __name__== "__main__":
    main()