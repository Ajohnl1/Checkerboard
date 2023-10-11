import checkers


def game():
    size = int(input("Enter the size of the checkerboard: "))
    board = checkers.build_board(size)

    print("Checkerboard:")
    for row in board:
        print(row)

    empty_count = checkers.get_count(board, 'empty')
    red_count = checkers.get_count(board, 'red')
    black_count = checkers.get_count(board, 'black')

    print(f"Empty Cells: {empty_count}")
    print(f"Red Cells: {red_count}")
    print(f"Black Cells: {black_count}")


if __name__ == "__main__":
    game()
