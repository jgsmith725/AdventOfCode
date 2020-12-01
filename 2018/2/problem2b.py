import os

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    for line in lines:
        line = line.replace('\n','')
        f2=open(my_file, "r")
        lines2 = f2.readlines()

        for line2 in lines2:
            line2 = line2.replace('\n','')
            foundIdx = -1

            for idx in range(len(line)):
                if line[idx] != line2[idx]:
                    if foundIdx >= 0:  #we've found more than one character difference
                        foundIdx = -1
                        break
                    else:  #we've found a single character difference
                        foundIdx = idx

            if foundIdx >= 0:
                ans = ''
                for i in range(len(line)): 
                    if i != foundIdx: 
                        ans = ans + line[i] 
                print(ans)
                break
                
        if foundIdx >= 0:
            break
            



if __name__== "__main__":
    main()