

def calculate_heuristics(board):
    return number_of_black_tokens(board)


def number_of_black_tokens(board):
    num_black = board.count("1")
    return int(num_black)

