

def number_of_black_white(board):
    num_black = board.count("1")
    num_white = board.count("0")

    total = num_white - num_black
    return total