import os

class Directions:
    def __init__(self):
        self.node_dict = {}

        up_node = DirectionNode('u')
        right_node = DirectionNode('r')
        down_node = DirectionNode('d')
        left_node = DirectionNode('l')

        self.node_dict['u'] = up_node
        self.node_dict['r'] = right_node
        self.node_dict['d'] = down_node
        self.node_dict['l'] = left_node

        up_node.left = left_node
        up_node.right = right_node
        right_node.left = up_node
        right_node.right = down_node
        down_node.left = right_node
        down_node.right = left_node
        left_node.left = down_node
        left_node.right = up_node

    def getNewDirection(self, curr_dir, turn_dir):
        node = self.node_dict[curr_dir]
        if turn_dir == 'l':
            return node.left.dir
        elif turn_dir == 's':
            return node.dir
        else:
            return node.right.dir

class DirectionNode:
    def __init__(self, dir):
        self.dir = dir
        self.left = None
        self.right = None

class Cart:
    def __init__(self, loc, dir, directions):
        self.loc = loc
        self.dir = dir
        self.directions = directions
        self.next_turn = 'l'
        self.cruisin_and_boozin = True

    def turn(self, turn_dir):
        self.dir = self.directions.getNewDirection(self.dir, turn_dir)

    def move(self, grid):
        if self.dir == 'l':
            self.loc[0] -= 1
        elif self.dir == 'r':
            self.loc[0] += 1
        elif self.dir == 'u':
            self.loc[1] -= 1
        elif self.dir == 'd':
            self.loc[1] += 1

        next_track = grid[self.loc[1]][self.loc[0]]
        if next_track == '\\':
            if self.dir == 'l' or self.dir == 'r':
                self.turn('r')
            else:
                self.turn('l')
        elif next_track == '/':
            if self.dir == 'l' or self.dir == 'r':
                self.turn('l')
            else:
                self.turn('r')
        elif next_track == '+':
            self.turn(self.next_turn)
            if self.next_turn == 'l':
                self.next_turn = 's'
            elif self.next_turn == 's':
                self.next_turn = 'r'
            else:
                self.next_turn = 'l'

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')
    f=open(my_file, "r")
    lines = f.readlines()

    carts = []
    grid = []
    y = 0
    directions = Directions()
    for line in lines:
        row = []
        x = 0
        for char in line:
            row.append(char)
            if char == '^':
                carts.append(Cart([x, y], 'u', directions))
            elif char == '<':
                carts.append(Cart([x, y], 'l', directions))
            elif char == '>':
                carts.append(Cart([x, y], 'r', directions))
            elif char == 'v':
                carts.append(Cart([x, y], 'd', directions))
            x += 1
        y += 1
        grid.append(row)

    moving = True
    while moving:
        num_alive = 0
        for cart in carts:
            cart.move(grid)
            collision_loc = getCollisionLoc(carts)
            if collision_loc is not None:
                for cart in carts:
                    if cart.loc == collision_loc:
                        cart.cruisin_and_boozin = False
            if cart.cruisin_and_boozin == True:
                num_alive += 1
                last_cart_alive = cart

        if num_alive == 1:
            moving = False
            print(last_cart_alive.loc)
    
def getCollisionLoc(carts):
    locs = []
    for cart in carts:
        if cart.cruisin_and_boozin == False:
            continue
        if cart.loc in locs:
            return cart.loc
        else:
            locs.append(cart.loc)
    return None

if __name__== "__main__":
    main()