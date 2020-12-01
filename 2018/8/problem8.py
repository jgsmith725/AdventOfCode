import os

class Node:
    def __init__(self, header):
        self.header = header
        self.children = []
        self.metadata = []

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()

    license_nums = lines[0].split(' ')
    stack = []
    for idx in range(len(license_nums)-1, -1, -1):
        stack.append(int(license_nums[idx]))

    head_node = Node([stack.pop(), stack.pop()])
    handleNode(head_node, stack)
    
    #part1
    #print(getMetadata(head_node))

    #part2
    print(getMetadataWithIndicies(head_node))

def handleNode(node, stack):
    num_children = node.header[0]
    num_metadata = node.header[1]

    for cnt in range(0, num_children):
        child = Node([stack.pop(), stack.pop()])
        node.children.append(child)
        handleNode(child, stack)
    
    for cnt in range(0, num_metadata):
        new_metadata = stack.pop()
        node.metadata.append(new_metadata)

def getMetadata(node):
    num_metadata = 0
    for child in node.children:
        num_metadata += getMetadata(child)

    for metadata in node.metadata:
        num_metadata += metadata

    return num_metadata

def getMetadataWithIndicies(node):
    num_metadata = 0
    if len(node.children) == 0:
        for metadata in node.metadata:
            num_metadata += metadata
    else:
        for metadata in node.metadata:
            metadata -= 1 #metadatas are 1 indexed, this makes them 0 indexed
            if metadata < len(node.children):
                num_metadata += getMetadataWithIndicies(node.children[metadata])
    return num_metadata

        
if __name__== "__main__":
    main()