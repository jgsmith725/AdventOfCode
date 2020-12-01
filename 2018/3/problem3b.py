import os
import numpy as np

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    fabric = np.zeros((1000,1000))
    overlap = 0
    clean_claims = {}

    for line in lines:
        line = line.split(' ')
        claim_id = int(line[0].split('#')[1])
        left_margin = int(line[2].split(',')[0])
        top_margin = int(line[2].split(',')[1].split(':')[0])
        width = int(line[3].split('x')[0])
        height = int(line[3].split('x')[1])

        clean_claims[claim_id] = 1

        for x in range(left_margin, left_margin + width):
            for y in range(top_margin, top_margin + height):
                val = int(fabric[x,y])

                if val > 0:
                    overlapped_claim = fabric[x][y]
                    clean_claims[overlapped_claim] = 0
                    clean_claims[claim_id] = 0
                    fabric[x][y] = -1
                    overlap += 1
                elif val == -1:
                    clean_claims[claim_id] = 0
                else:
                    fabric[x][y] = claim_id
            
    print('overlap = ' + str(overlap))
    for key in clean_claims:
        if clean_claims[key] == 1:
            print('clean claim = ' + str(key))

if __name__== "__main__":
    main()