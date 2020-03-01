from math import sqrt, ceil


def calculate_heuristics(board, heuristic_num):
    if str(heuristic_num) == '1':
        return number_of_black(board)

    if str(heuristic_num) == '2':
        return number_of_black_over_five(board)

    if str(heuristic_num) == '3':
        return max_adjacent_black(board)


def number_of_black(board):
    num_black = board.count("1")
    return int(num_black)


def number_of_black_over_five(board):
    num_black = board.count("1")
    return ceil(num_black/5)


def max_adjacent_black(board):
    length = int(len(board))
    n = int(sqrt(length))
    number_of_blacks = number_of_black(board)
    max_adjacent = 1

    # Solution found
    if number_of_blacks == 0:
        return 0

    # Iterate through the whole board
    for i in range(0, length):
        adjacent_black = 0
        token_above = i - n
        token_below = i + n
        token_left = i - 1
        token_right = i + 1

        # Only check for adjacent if the token itself is black
        if board[i] == '1':
            adjacent_black += 1
            # Check for adjacent
            if token_above > 0:
                if board[token_above] == '1':
                    adjacent_black += 1
            if token_below < length:
                if board[token_below] == '1':
                    adjacent_black += 1
            if token_left > 0:
                if board[token_left] == '1':
                    adjacent_black += 1
            if token_right < length:
                if board[token_right] == '1':
                    adjacent_black += 1

        # Update the max adjacent value if a higher adjacent value is found
        if adjacent_black > max_adjacent:
            max_adjacent = adjacent_black

    ratio = number_of_blacks/max_adjacent

    return int(ratio*number_of_blacks)
