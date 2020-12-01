import os
import math

class Chemical:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Equation:
    def __init__(self, product, reactants):
        self.product = product
        self.reactants = reactants

def getEquationsDict():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    equations={} #keys are products, values are arrays of reactants
    excessDict = {} #keys are the products, values are the amount of excess

    for line in lines:
        equationStr = line.split(' => ')
        reactantsStr = equationStr[0].split(', ')
        productStr = equationStr[1].split('\n')[0].split(' ')

        reactants = []
        for reactantStr in reactantsStr:
            reactant = Chemical(reactantStr.split(' ')[1], int(reactantStr.split(' ')[0]))
            reactants.append(reactant)

        eq = Equation(Chemical(productStr[1], int(productStr[0])),  reactants)

        equations[productStr[1]] = eq
        excessDict[productStr[1]] = 0
  
    return equations, excessDict

def getNeededOre(productName, neededAmount, excessDict, equations):
    currEq = equations[productName]
    neededOre = 0

    #use existing excess
    neededAmount -= excessDict[productName]
    if neededAmount < 0:
        excessDict[productName] = abs(neededAmount)
        neededAmount = 0
    else:
        excessDict[productName] = 0

    #calculate the amount we need to produce and if there is any excess
    numReactions = math.ceil(neededAmount / currEq.product.amount)
    excess = currEq.product.amount * numReactions - neededAmount
    excessDict[currEq.product.name] += excess

    #traverse down the tree
    for reactant in currEq.reactants:
        if reactant.name == 'ORE':
            neededOre += reactant.amount * numReactions
        else:
            neededOre += getNeededOre(reactant.name, reactant.amount * numReactions , excessDict, equations)
    
    return neededOre

def main():
    [equations, excessDict] = getEquationsDict()
    print(getNeededOre('FUEL', 3061522, excessDict, equations))
    print(getNeededOre('FUEL', 3061523, excessDict, equations))
    print(getNeededOre('FUEL', 3061524, excessDict, equations))
    currGuess = 1000000000000
    ub = 1000000000000
    lb = 0
    found = True
    while not found:
        ore = getNeededOre('FUEL', currGuess, excessDict, equations)
        print('ore = ' + str(ore) + ' currGuess = ' + str(currGuess))
        if ore > 1000000000000:
            ub = currGuess
            currGuess = round(((currGuess - lb) / 2) + lb)
        elif ore < 1000000000000:
            lb = currGuess
            currGuess = round(((ub - currGuess) / 2) + currGuess)

        if abs(currGuess - ub) <= 1:
            print('Found = ' + str(currGuess))
            foundore = getNeededOre('FUEL', currGuess, excessDict, equations)
            print('Found ore = ' + str(foundore))
            found = True
        
if __name__== "__main__":
    main()