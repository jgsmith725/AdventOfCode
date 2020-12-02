import os

def parseInput(line):
    mn = int(line.split("-")[0])
    mx = int(line.split("-")[1].split(" ")[0])
    letter=line.split(":")[0].split(" ")[1]
    password=line.split(": ")[1]
    return [mn, mx, letter, password]

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()
    numValid1 = 0
    numValid2 = 0
    for line in lines:
        [mn, mx, letter, password] = parseInput(line)

        #Part 1
        numChar = 0
        for char in password:
            if char == letter:
              numChar = numChar + 1
        
        if numChar >= mn and numChar <= mx:
            numValid1 = numValid1 + 1
        
        #Part 2
        numFound = 0
        if password[mn - 1] == letter:
            numFound = numFound + 1
        if password[mx - 1] == letter:
            numFound = numFound + 1
        if numFound == 1:
            numValid2 = numValid2 + 1

    print(str(numValid1) + " " + str(numValid2))


if __name__== "__main__":
    main()