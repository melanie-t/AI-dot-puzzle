

def calculate_heuristics(board, index):
    return number_of_black_tokens(board)
    # return adjacencies(board, index)
    # return isolated(board, index)


def number_of_black_tokens(board):
    num_black = board.count("1")
    return int(num_black)


# TODO PATRICK
def adjacency(board, index):
    print()


# TODO GUENOLE
def isolated(board, index):
    print()

