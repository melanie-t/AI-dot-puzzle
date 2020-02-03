

def create_child_nodes(initial_node):
    print("Creating child nodes")
    # TODO Implement node creating


def flip_token(token):
    if token == '0':
        return '1'
    else:
        return '0'


def flip_adjacent_nodes(board, n, index):
    max_index = n-1
    token_above = index-n
    token_below = index+n
    token_left = index-1
    token_right = index+1

    # Top left corner
    if index == 0:
        board[index] = flip_token(board[index])
        board[token_right] = flip_token(board[token_right])
        board[token_below] = flip_token(board[token_below])

    # Top right corner
    elif index == max_index:
        board[index] = flip_token(board[index])
        board[token_left] = flip_token(board[token_left])
        board[token_below] = flip_token(board[token_below])

    # Bottom left corner
    elif index == n*max_index:
        board[index] = flip_token(board[index])
        board[token_above] = flip_token(board[token_above])
        board[token_right] = flip_token(board[token_right])

    # Bottom right Corner
    elif index == n*n-1:
        board[index] = flip_token(board[index])
        board[token_above] = flip_token(board[token_above])
        board[token_left] = flip_token(board[token_left])

    # Left edge
    elif index % n == 0:
        board[index] = flip_token(board[index])
        board[token_above] = flip_token(board[token_above])
        board[token_below] = flip_token(board[token_below])
        board[token_right] = flip_token(board[token_right])

    # Right edge
    elif (index+1) % n == 0:
        board[index] = flip_token(board[index])
        board[token_above] = flip_token(board[token_above])
        board[token_below] = flip_token(board[token_below])
        board[token_left] = flip_token(board[token_left])

    # Top edge
    elif index < max_index:
        board[index] = flip_token(board[index])
        board[token_left] = flip_token(board[token_left])
        board[token_right] = flip_token(board[token_right])
        board[token_below] = flip_token(board[token_below])

    # Bottom edge
    elif int(index/n) == max_index:
        board[index] = flip_token(board[index])
        board[token_above] = flip_token(board[token_above])
        board[token_left] = flip_token(board[token_left])
        board[token_right] = flip_token(board[token_right])

    # All inner tokens
    else:
        board[index] = flip_token(board[index])
        board[token_above] = flip_token(board[token_above])
        board[token_below] = flip_token(board[token_below])
        board[token_left] = flip_token(board[token_left])
        board[token_right] = flip_token(board[token_right])


# TODO Implement txt file parser
