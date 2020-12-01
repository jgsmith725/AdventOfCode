import os

class Pot:
    def __init__(self, value, has_plant):
        self.value = value
        self.has_plant = has_plant
        self.left = None
        self.right = None

    def addLeft(self, pot):
        self.left = pot
        pot.right = self
    
    def addRight(self, pot):
        self.right = pot
        pot.left = self

    def getLeft(self):
        if self.left == None:
            pot = Pot(self.value - 1, False)
            pot.right = self
            return pot
        else:
            return self.left
    
    def getRight(self):
        if self.right == None:
            pot = Pot(self.value + 1, False)
            pot.left = self
            return pot
        else:
            return self.right

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')
    f=open(my_file, "r")
    lines = f.readlines()
    state = lines[0].split('initial state: ')[1].replace('\n', '')

    spread_dict = {}
    for idx in range(2, len(lines)):
        spread = lines[idx].split(' => ')
        spread_dict[spread[0]] = spread[1].replace('\n', '')

    for index in range(len(state)):
        if index == 0:
            leftmost_pot = Pot(index, state[index] == '#')
            curr_pot = leftmost_pot
        else:
            curr_pot.addRight(Pot(index, state[index] == '#'))
            curr_pot = curr_pot.right

    prev_tot = 0

    for gen in range(0,500):
        tot = getTotal(leftmost_pot)
        #if gen % 1000 == 0:
        print('gen = ' + str(gen) + ' tot = ' + str(tot) + ' diff = ' + str(tot - prev_tot))
        prev_tot = tot

        #printPots(leftmost_pot)
        leftmost_pot = spreadPlants(leftmost_pot, spread_dict)

def spreadPlants(leftmost_pot, spread_dict):  
    leftmost_pot.addLeft(Pot(leftmost_pot.value - 1, False))
    leftmost_pot.left.addLeft(Pot(leftmost_pot.value - 2, False))
    curr_pot = leftmost_pot.left.left

    searching = True
    first_found = False
    new_gen_curr_pot = None
    while searching:
        has_plant = advanceGen(curr_pot, spread_dict)
        if new_gen_curr_pot is not None:
            new_gen_curr_pot.addRight(Pot(curr_pot.value, has_plant))
            new_gen_curr_pot = new_gen_curr_pot.right
            
        if not first_found and has_plant:
            new_gen_leftmost_pot = Pot(curr_pot.value, has_plant)
            new_gen_curr_pot = new_gen_leftmost_pot
            first_found = True
        
        if curr_pot.right == None:
            if advanceGen(curr_pot.getRight().getRight(), spread_dict) == True:
                new_gen_curr_pot.addRight(Pot(new_gen_curr_pot.value + 1, advanceGen(curr_pot.getRight(), spread_dict)))
                new_gen_curr_pot.right.addRight(Pot(new_gen_curr_pot.value + 2, True))
            elif advanceGen(curr_pot.getRight(), spread_dict) == True:
                new_gen_curr_pot.addRight(Pot(new_gen_curr_pot.value + 1, True))
            searching = False
        else:
            curr_pot = curr_pot.right

    return new_gen_leftmost_pot

def advanceGen(pot, spread_dict):
    key = getKey(pot)
    
    if spread_dict[key] == '#':
    #if key in spread_dict:
        return True
    else:
        return False

    
def getKey(pot):
    if pot.getLeft().getLeft().has_plant:
        char1 = '#'
    else:
        char1 = '.'
    if pot.getLeft().has_plant:
        char2 = '#'
    else:
        char2 = '.'
    if pot.has_plant:
        char3 = '#'
    else:
        char3 = '.'
    if pot.getRight().has_plant:
        char4 = '#'
    else:
        char4 = '.'
    if pot.getRight().getRight().has_plant:
        char5 = '#'
    else:
        char5 = '.'
    return char1 + char2 + char3 + char4 + char5

def getTotal(leftmost_pot):
    curr_pot = leftmost_pot
    tot = 0
    while curr_pot is not None:
        if curr_pot.has_plant:
            tot += curr_pot.value
        curr_pot = curr_pot.right
    return tot

def printPots(leftmost_pot):
    curr_pot = leftmost_pot
    output = ''
    while curr_pot is not None:
        if curr_pot.value == 0:
            output += '0'
        elif curr_pot.has_plant:
            output += '#'
        else:
            output += '.'  
        curr_pot = curr_pot.right

    print(output)

if __name__== "__main__":
    main()