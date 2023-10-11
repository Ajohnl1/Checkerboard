if __name__ == "__main__":
    print("This is not intended to be run as main")

from numpy import random


# building board
def build_board(size):
    board = random.choice(['empty', 'red', 'black'], size=(size, size))
    return board


def get_count(board, color):
    return(board == color).sum()



