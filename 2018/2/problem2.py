import os

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    doubles_tot = 0
    triples_tot = 0

    for line in lines:
        chardict = {}
        chardict['\n'] = 4

        for char in line:
            if char in chardict:
                chardict[char] += 1
            else:
                chardict[char] = 1

        double_found = False
        triple_found = False

        for key in chardict:
            if chardict[key] == 2 and double_found == False:
                doubles_tot += 1
                double_found = True
            elif chardict[key] == 3 and triple_found == False:
                triples_tot += 1
                triple_found = True

    
    checksum = doubles_tot * triples_tot
    print(checksum)

            





if __name__== "__main__":
    main()