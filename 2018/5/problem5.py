import os
import numpy as np

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    polymer = lines[0]
    print(getPolymerLength(polymer, 'vector'))
    
def getPolymerLength(polymer, method_type):
    if (method_type == 'string_parse'):
        return stringLoop(polymer)
    if (method_type == 'vector'):
        polymer_vec = getPolymerVec(polymer)
        #part 1 return len(reactVectorPolymer(polymer_vec))
        reacted_polymer_vec = reactVectorPolymer(polymer_vec)
        smallest_vec = -1
        #part2
        for unit in range(1,27):
            removed_vec = removeUnitsFromPolymerVec(unit, reacted_polymer_vec)
            reacted_removed_vec = reactVectorPolymer(removed_vec)
            if smallest_vec == -1 or len(reacted_removed_vec) < smallest_vec:
                smallest_vec = len(reacted_removed_vec)
    return 'smallest reacted = ' + str(smallest_vec)

def convertCharToUnit(char):
    if (ord(char) < ord('a')):
        unit = ord(char) - (ord('A') - 1)
    else:
        unit = (ord(char) - (ord('a') - 1)) * -1
    return unit

def removeUnitsFromPolymerVec(unit, polymer_vec):
    unit_locs = np.argwhere(polymer_vec == unit)
    unit_locs = np.append(unit_locs, np.argwhere(polymer_vec == (unit * -1)))
    return np.delete(polymer_vec, unit_locs)
    

def getPolymerVec(polymer):
    polymer_vec = np.zeros(len(polymer), dtype=int)
    for idx in range(0, len(polymer)):
        polymer_vec[idx] = convertCharToUnit(polymer[idx])
    return polymer_vec

def getReactedUnitLocs(added_polymer):
    zero_locs = np.where(added_polymer == 0)[0]
    if len(zero_locs) == 0:
        return zero_locs
    zero_locs_shifted = np.add(zero_locs, np.negative(np.ones(len(zero_locs), dtype=int)))
    zero_locs = np.append(zero_locs, zero_locs_shifted)
    sorted_zero_locs = np.sort(zero_locs)
    prev_loc = -1
    deletions = []
    for idx in range(len(sorted_zero_locs)):
        curr_loc=sorted_zero_locs[idx]
        if curr_loc == prev_loc:
            deletions.append(idx)
            deletions.append(idx + 1)
            idx += 1
            prev_loc = -1
            continue
        prev_loc = curr_loc
    sorted_zero_locs = np.delete(sorted_zero_locs, deletions)
    return sorted_zero_locs

def reactVectorPolymer(polymer_vec):
    while(True):
        shifted_polymer = np.insert(polymer_vec, 0, 0)
        shifted_polymer = np.delete(shifted_polymer, len(shifted_polymer) - 1)
        added_polymer = np.add(polymer_vec, shifted_polymer)
        reacted_unit_locs = getReactedUnitLocs(added_polymer)
        if len(reacted_unit_locs) == 0:
            break
        polymer_vec = np.delete(polymer_vec, reacted_unit_locs)
    return polymer_vec
     
def stringLoop(polymer):
    skip_indicies = set()
    iter = 0
    done = False
    while not done:
        iter += 1
        print('iter = ' + str(iter))

        prev_unit = ' '
        prev_unit_idx = 0
        reaction_occured = False
        for idx in range(0, len(polymer)):
            if idx in skip_indicies:
                continue

            unit = polymer[idx]
            if unit != prev_unit and unit.lower() == prev_unit.lower():
                reaction_occured = True
                skip_indicies.add(idx)
                skip_indicies.add(prev_unit_idx)
                break

            prev_unit = unit
            prev_unit_idx = idx

        if not reaction_occured:
            done = True

    num_reacted = len(skip_indicies)
    num_remaining = len(polymer) - num_reacted
    return num_remaining

if __name__== "__main__":
    main()