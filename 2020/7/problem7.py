import os

class Bag:
    def __init__(self, color):
        self.color = color
        self.parents = []
        self.children = []
        self.child_counts = []
        self.counted = False
    

def parseInput(line, bag_dict):
    color = line.split(" bags contain")[0]
    if color in bag_dict:
        curr_bag = bag_dict[color]
    else:
        curr_bag = Bag(color)
        bag_dict[color] = curr_bag

    children = line.split(" bags contain")[1].split(".")[0].split(",")

    for child in children:
        child_color = child.split(" bag")[0].split(" ")[2:]
        child_color = " ".join(child_color)
        if child_color == "other":
            continue
        child_num = int(child.split(" ")[1])
        if child_color in bag_dict:
            child_inst = bag_dict[child_color]
        else:
            child_inst = Bag(child_color)
            bag_dict[child_color] = child_inst

        child_inst.parents.append(curr_bag)
        curr_bag.children.append(child_inst)
        curr_bag.child_counts.append(child_num)

def countParents(bag):
    if len(bag.parents) == 0:
        return 0
    count = 0
    for parent in bag.parents:
        if (parent.counted == True):
            continue
        parent.counted = True
        count = count + 1 + countParents(parent)
    return count

def countChildren(bag):
    if len(bag.children) == 0:
        return 0
    count = 0
    for idx in range(len(bag.children)):
        child = bag.children[idx]
        child_count = bag.child_counts[idx]
        count = count + child_count + child_count * countChildren(child)
    return count


def part1(lines):
    bag_dict = {}
    for line in lines:
        parseInput(line, bag_dict)
    
    return countParents(bag_dict["shiny gold"])

def part2(lines):
    bag_dict = {}
    for line in lines:
        parseInput(line, bag_dict)

    #print(countChildren(bag_dict["faded blue"]))
    #print(countChildren(bag_dict["dark olive"]))
    #print(countChildren(bag_dict["vibrant plum"]))
    return countChildren(bag_dict["shiny gold"])

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    #print(part1(lines))
    print(part2(lines))
    

if __name__== "__main__":
    main()