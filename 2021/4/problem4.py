import os
import numpy as np

def part1(draws, boards, board_hits):
    for draw in draws:
        indices = np.where(boards == draw)
        for ln in range(len(indices[0])):
            board_hits[indices[0][ln]][indices[1][ln]][indices[2][ln]] = 0
        winners = checkBoards(board_hits)
        if len(winners) == 1:
            print(getUnmarkedSum(boards[winners[0]], board_hits[winners[0]]) * draw)
            break
        

def checkBoards(boards):
    winners = []
    for board_idx in range(len(boards)):
        found = False
        board = boards[board_idx]
        for row in board:
            if np.all(row == 0):
                found = True
        for col_idx in range(len(board[0])):
            col = board[:, col_idx]
            if np.all(col == 0):
                found = True
        if found:
            winners.append(board_idx)
    return winners

def getUnmarkedSum(board, board_hit):
    return np.sum(np.multiply(board, board_hit))

def part2(draws, boards, board_hits):
    loser_idx = -1
    for draw in draws:
        indices = np.where(boards == draw)
        for ln in range(len(indices[0])):
            board_hits[indices[0][ln]][indices[1][ln]][indices[2][ln]] = 0
        winners = checkBoards(board_hits)
        if len(winners) == len(boards) - 1:
            for idx in range(len(boards)):
                if not idx in winners:
                    loser_idx = idx
                    break
        if len(winners) == len(boards):
             print(getUnmarkedSum(boards[loser_idx], board_hits[loser_idx]) * draw)
             break
def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data.txt')

    f=open(my_file, "r")
    lines = f.readlines()
    draws = [int(string) for string in lines[0].split(",")]
    boards = []
    board_hits = []
    for line_idx in range(1,len(lines)):
        line = lines[line_idx]
        if line == '\n':
            if line_idx != 1:
                boards.append(board)
                board_hits.append(board_hit)
            board = []
            board_hit = []
        else:
            board.append([int(string) for string in list(line.split())])
            board_hit.append([1, 1, 1, 1, 1])

    #part1(draws, np.array(boards), np.array(board_hits))
    part2(draws, np.array(boards), np.array(board_hits))



if __name__== "__main__":
    main()