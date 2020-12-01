import os

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')
    freqs = []
    searching = True
    total = 0
    while(searching):
        f=open(my_file, "r")
        lines = f.readlines()
        for line in lines:
            line = line.split('\n',1)[0]
            if line[0] == '+':
                total += int(line[1:])
            else:
                total -= int(line[1:])

            if total in freqs:
                searching = False
                print(total)
                break
            else:
                freqs.append(total)

if __name__== "__main__":
    main()