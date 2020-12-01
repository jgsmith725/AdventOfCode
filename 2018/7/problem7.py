import os

class Node:
    def __init__(self, name):
        self.children = []
        self.parents = []
        self.name = name

    def addChild(self, node):
        if node not in self.children:
            self.children.append(node)

    def addParent(self, node):
        if node not in self.parents:
            self.parents.append(node)

class Worker:
    def __init__(self):
        self.time_left = 0
        self.current_step = None

    def assignWork(self, current_step):
        self.current_step = current_step
        self.time_left = self.getStepTime(current_step)

    def work(self):
        finished_step = None
        if self.time_left > 0:
            self.time_left -= 1
        else:
            finished_step = self.current_step
            self.current_step = None
        return finished_step

    def getStepTime(self, node):
        return ord(node.name) - ord('A') + 60


def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    #print(part1(lines))
    print(part2(lines))

def part2(lines):
    node_dict = setupNodes(lines)
    options = getInitialOptions(node_dict)
    second = 0
    workers = [Worker(), Worker(), Worker(), Worker(), Worker()]
    steps_done = []
    output = ""
    while True:
        for worker in workers:
            if worker.current_step is None:        
                lowest_node = popLowestNode(options, steps_done)
                if lowest_node is None:
                    break
                worker.assignWork(lowest_node)

        #print(str(second) + " " + getStepNameSafe(workers[0].current_step) + " " + getStepNameSafe(workers[1].current_step) + " " + output)

        if allWorkersDone(workers) == True:
            break

        second += 1

        for worker in workers:
            finished_step = worker.work()
            if finished_step is not None:
                output = output + finished_step.name
                if finished_step not in steps_done:
                    steps_done.append(finished_step)

    return('output = ' + output + ' time = ' + str(second))

def getStepNameSafe(Node):
    if Node is None:
        return "."
    else:
        return Node.name

def allWorkersDone(workers):
    all_done = True
    for worker in workers:
        if worker.current_step is not None:
            all_done = False
            break
    return all_done


def part1(lines):
    node_dict = setupNodes(lines)
    options = getInitialOptions(node_dict)

    output = ""
    done = False
    steps_done = []
    while True:
        lowest_node = popLowestNode(options, steps_done)
        if lowest_node is None:
            break
        steps_done.append(lowest_node)
        output = output + lowest_node.name

    return output


def setupNodes(lines):
    node_dict = {}
    for line in lines:
        steps = line.split(' must be finished before step ')
        parent = steps[0].split('Step ')[1]
        child = steps[1].split(' can begin.')[0]

        if parent not in node_dict:
            node_dict[parent] = Node(parent)
        if child not in node_dict:
            node_dict[child] = Node(child)

        parent = node_dict[parent]
        child = node_dict[child]

        parent.addChild(child)
        child.addParent(parent)
    return node_dict

def getInitialOptions(node_dict):
    options = []
    for key in node_dict:
        node = node_dict[key]
        if len(node.parents) == 0:
            options.append(node)
    return options
            
def popLowestNode(options, steps_done):
    firstNode = True
    if len(options) == 0:
        return None
    lowest_node = None
    for node in options:
        if isValidNode(node, steps_done):
            if firstNode == True:
                lowest_node = node
                firstNode = False
            elif ord(node.name) < ord(lowest_node.name):
                lowest_node = node
    if lowest_node == None:
        return None

    options.remove(lowest_node)
    for child in lowest_node.children:
        if child not in steps_done and child not in options:
            options.append(child)
    return lowest_node

def isValidNode(node, steps_done):
    valid = True
    for parent in node.parents:
        if parent not in steps_done:
            valid = False
            break
    return valid


if __name__== "__main__":
    main()