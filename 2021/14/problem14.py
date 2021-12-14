import os
import numpy as np
import collections

def parseInput(lines):
    polymer = lines[0].replace("\n","")
    rules = {}
    for idx in range(2,len(lines)):
        pair = str(lines[idx]).replace("\n","").split(" -> ")[0]
        insertion = str(lines[idx]).replace("\n","").split(" -> ")[1]
        rules[pair] = insertion
    return polymer, rules

def part1(lines):
    polymer, rules = parseInput(lines)
    for step in range(10):
        polymer = doInsert(polymer, rules)
    most_common = collections.Counter(polymer).most_common(1)[0]
    res = collections.Counter(polymer)
    least_common = min(res, key = res.get) 
    print(most_common[1] - str(polymer).count(least_common))

def doInsert(polymer, rules):
    idx = 0
    while idx < len(polymer) - 1:
        pair = str(polymer[idx]) + str(polymer[idx + 1])
        insertion = rules[pair]
        polymer = polymer[:idx + 1] + insertion + polymer[idx + 1:]
        idx += 2
    return polymer

def doInsert2(rules, rule_counts: dict):
    new_counts = {}
    for pair in rule_counts.keys():
        count = rule_counts[pair]
        letter_0 = pair[0]
        letter_1 = pair[1]
        insertion = rules[pair]
        new_pair_0 = "".join([letter_0, insertion])
        new_pair_1 = "".join([insertion, letter_1])
        if new_pair_0 in new_counts.keys():
            new_counts[new_pair_0] += count
        else:
            new_counts[new_pair_0] = count
        if new_pair_1 in new_counts.keys():
            new_counts[new_pair_1] += count
        else:
            new_counts[new_pair_1] = count
    return new_counts

def getCountsFromPolymer(polymer):
    rule_counts = {}
    idx = 0
    while idx < len(polymer) - 1:
        pair = str(polymer[idx]) + str(polymer[idx + 1])
        if pair in rule_counts.keys():
            rule_counts[pair] += 1
        else:
            rule_counts[pair] = 1
        idx += 1
    return rule_counts

def countLetters(rule_counts):
    letter_counts = {}
    for pair in rule_counts.keys():
        letter_0 = pair[0]
        letter_1 = pair[1]
        count = rule_counts[pair]
        if letter_0 in letter_counts.keys():
            letter_counts[letter_0] += count
        else:
            letter_counts[letter_0] = count
        if letter_1 in letter_counts.keys():
            letter_counts[letter_1] += count
        else:
            letter_counts[letter_1] = count
    return letter_counts

def part2(lines):
    polymer, rules = parseInput(lines)
    rule_counts = getCountsFromPolymer(polymer)

    for step in range(40):
        rule_counts = doInsert2(rules, rule_counts)
    
    letter_counts = countLetters(rule_counts)
    most_common = max(letter_counts.values())
    least_common = min(letter_counts.values()) 
    print(str((most_common - least_common)/ 2))


def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'test.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    #part1(lines)
    part2(lines)



if __name__== "__main__":
    main()
