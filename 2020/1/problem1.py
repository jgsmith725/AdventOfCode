import os

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()
    for line in lines:
        for line2 in lines:
            for line3 in lines:
                if int(line)+int(line2)+int(line3) == 2020:
                    print(str(line) + " " + str(line2) + " " + str(line3))
                    break

if __name__== "__main__":
    main()