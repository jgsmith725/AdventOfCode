import os

def part1():
    starting = [0,6,1,7,2,19,20]
    #starting = [0,3,6]
    speak_dict = {}
    turn = 0
    curr = None
    while True:
        if curr is not None:
            prev = curr
        if turn < len(starting):
            prev = starting[turn]
            speak_dict[prev] = [turn]
        else:
            if prev in speak_dict and len(speak_dict[prev]) == 2:
                curr = speak_dict[prev][1] - speak_dict[prev][0]
            else:
                curr = 0
            
            if curr in speak_dict and len(speak_dict[curr]) == 2:
                speak_dict[curr][0] = speak_dict[curr][1]
                speak_dict[curr][1] = turn
            elif curr in speak_dict and len(speak_dict[curr]) == 1:
                speak_dict[curr].append(turn)
            else:
                speak_dict[curr] = [turn]
      
        turn = turn + 1
        if turn == 30000000:
            break
    return curr

def main():
    print(part1())
    

if __name__== "__main__":
    main()