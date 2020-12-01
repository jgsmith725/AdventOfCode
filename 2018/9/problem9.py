import numpy as np

class Circle():
    def __init__(self, starting_marble):
        self.current_marble = starting_marble
    
    def getLeft(self,  count):
        marble = self.current_marble
        for i in range(0,count):
            marble = marble.left
        return marble

    def getRight(self, count):
        marble = self.current_marble
        for i in range(0,count):
            marble = marble.right
        return marble

    def insertLeft(self, marble, count):
        current_marble = self.getLeft(count)
        marble.left = current_marble.left
        current_marble.left.right = marble
        marble.right = current_marble
        current_marble.left = marble

    def insertRight(self, marble, count):
        current_marble = self.getRight(count)
        marble.right = current_marble.right
        current_marble.right.left = marble
        marble.left = current_marble
        current_marble.right = marble

    def removeLeft(self, count):
        marble = self.getLeft(count)
        self.removeMarble(marble)
        return marble

    def removeRight(self, count):
        marble = self.getRight(count)
        self.removeMarble(marble)
        return marble

    def removeMarble(self, marble):
        marble.left.right = marble.right
        marble.right.left = marble.left
        marble.left = None
        marble.right = None

class Marble():
    def __init__(self, value):
        self.value = value
        self.   left = None
        self.right = None

def main():
    num_players = 424
    num_points = 7114400

    marble = Marble(0)
    marble.right = marble
    marble.left = marble
    circle = Circle(marble)

    players = np.zeros(num_players)
    curr_player = 0
    for turn in range(1,num_points+1):
        new_marble = Marble(turn)
        if turn % 23 == 0:
            curr_player = turn % num_players
            players[curr_player] += turn
            players[curr_player] += circle.removeLeft(7).value
            circle.current_marble = circle.getLeft(6)
        else:
            circle.insertRight(new_marble, 1)
            circle.current_marble = new_marble

    winner = np.argmax(players)
    winning_score = players[winner]

    print(winning_score)

if __name__== "__main__":
    main()