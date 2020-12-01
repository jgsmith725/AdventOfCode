import os

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')
    f=open(my_file, "r")
    lines = f.readlines()

    state = lines[0].split('initial state: ')[1].replace('\n', '')
    state = '........................................' + state + '........................................'
    state = list(state)
    spread_dict = {}
    for idx in range(2, len(lines)):
        spread = lines[idx].split(' => ')
        spread_dict[spread[0]] = spread[1].replace('\n', '')

    separator = ''
    searching = True
    gen = 0
    tots = []
    tot = 0
    diffs = []

    index = 0   
    for gen in range(0,20000):
        gen += 1
        index -=4
        new_state = ['.', '.', '.', '.']

        for idx in range(0, len(state) - 4):
            plants = state[idx:idx+5]
            key = separator.join(plants)
            #if key in spread_dict:
            #    new_state.append('#')
            #else:
            #    new_state.append('.')
            new_state.append(spread_dict[key])
        new_state.append('.')
        new_state.append('.')
        new_state.append('.')
        new_state.append('.')
        #print(new_state)
        state = new_state
        #print(str(gen + 1) + ': ' + str(state[37:len(state)-39]))
        prev_tot = tot
        tot = getPlantTotal(state, index)
        diff = tot - prev_tot

        #if tot in tots:
            #searching = False
            #print('found duplicate tot ' + str(tot) + ' at gen ' + str(gen))
        #else:
        #    tots.append(tot)

        #if diff in diffs:
            #searching = False
            #print('found duplicate diff ' + str(diff) + ' at gen ' + str(gen))
        #else:
        #    diffs.append(diff)
        
        val = new_state[abs(index)]
        new_state[abs(index)] = '0'
        #print('gen: ' + str(gen) + ' total: ' + str(tot) + ' state ' + str(new_state))
        if gen % 1000 == 0:
            print('gen: ' + str(gen) + ' total: ' + str(tot))
        new_state[abs(index)] = val


def getPlantTotal(state, index):
    tot = 0
    for char in state:
        if char == '#':
            tot += index
        index += 1
    return tot

if __name__== "__main__":
    main()