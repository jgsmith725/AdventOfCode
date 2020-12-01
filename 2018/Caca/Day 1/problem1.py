import os

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')
    f=open(my_file, "r")
    lines = f.readlines()
    frequency=0
    frequencies_found=[]
    done=False
    while True:
        for line in lines:
            if line[0]=='-':
                newstring_arr=line.split('-')
                newstring_arr=newstring_arr[1].split('\n')
                new_string = newstring_arr[0]
                frequency=frequency-int(new_string)
            else : 
                newstring_arr=line.split('+')
                newstring_arr=newstring_arr[1].split('\n')
                new_string = newstring_arr[0]
                frequency=frequency+int(new_string)
            if frequency in frequencies_found :
                print('duplicate freq = ' + str(frequency))
                done=True
                break
            frequencies_found.append(frequency)
        if done==True:
            break
    print(str(frequency))

    

if __name__== "__main__":
    main()