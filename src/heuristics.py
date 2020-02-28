

def calculate_heuristics(board):
    return number_of_black(board)
    # return number_of_black_over_five(board)


def number_of_black(board):
    num_black = board.count("1")
    return int(num_black)


def number_of_black_over_five(board):
    num_black = board.count("1")
    return int(num_black/5)
