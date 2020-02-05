import math

def create_child_nodes(__initial_node, __open_list, __closed_list, __search_list):
    # Creates children of the initial
    print("Generated child nodes for ", __initial_node)
    for token in range(0, len(__initial_node)):
        __child_node = flip_adjacent_nodes(__initial_node, token)
        # Check to see if the node exists already
        __node_exists = __child_node in __open_list or __child_node in __closed_list
        if not __node_exists:
            # Add the child node to the open list and pop into search list stack
            print("\t\tDiscovered", __child_node)
            __open_list.append(__child_node)
            __search_list.append(__child_node)


def flip_token(token):
    if token == '0':
        return '1'
    else:
        return '0'


def flip_adjacent_nodes(board, index):
    # Copy the board to modify the new board
    new_board = list(board)
    n = int(math.sqrt(len(new_board)))
    max_index = n-1
    token_above = index-n
    token_below = index+n
    token_left = index-1
    token_right = index+1

    # Top left corner
    if index == 0:
        new_board[index] = flip_token(new_board[index])
        new_board[token_right] = flip_token(new_board[token_right])
        new_board[token_below] = flip_token(new_board[token_below])

    # Top right corner
    elif index == max_index:
        new_board[index] = flip_token(new_board[index])
        new_board[token_left] = flip_token(new_board[token_left])
        new_board[token_below] = flip_token(new_board[token_below])

    # Bottom left corner
    elif index == n*max_index:
        new_board[index] = flip_token(new_board[index])
        new_board[token_above] = flip_token(new_board[token_above])
        new_board[token_right] = flip_token(new_board[token_right])

    # Bottom right Corner
    elif index == n*n-1:
        new_board[index] = flip_token(new_board[index])
        new_board[token_above] = flip_token(new_board[token_above])
        new_board[token_left] = flip_token(new_board[token_left])

    # Left edge
    elif index % n == 0:
        new_board[index] = flip_token(new_board[index])
        new_board[token_above] = flip_token(new_board[token_above])
        new_board[token_below] = flip_token(new_board[token_below])
        new_board[token_right] = flip_token(new_board[token_right])

    # Right edge
    elif (index+1) % n == 0:
        new_board[index] = flip_token(new_board[index])
        new_board[token_above] = flip_token(new_board[token_above])
        new_board[token_below] = flip_token(new_board[token_below])
        new_board[token_left] = flip_token(new_board[token_left])

    # Top edge
    elif index < max_index:
        new_board[index] = flip_token(new_board[index])
        new_board[token_left] = flip_token(new_board[token_left])
        new_board[token_right] = flip_token(new_board[token_right])
        new_board[token_below] = flip_token(new_board[token_below])

    # Bottom edge
    elif int(index/n) == max_index:
        new_board[index] = flip_token(new_board[index])
        new_board[token_above] = flip_token(new_board[token_above])
        new_board[token_left] = flip_token(new_board[token_left])
        new_board[token_right] = flip_token(new_board[token_right])

    # All inner tokens
    else:
        new_board[index] = flip_token(new_board[index])
        new_board[token_above] = flip_token(new_board[token_above])
        new_board[token_below] = flip_token(new_board[token_below])
        new_board[token_left] = flip_token(new_board[token_left])
        new_board[token_right] = flip_token(new_board[token_right])

    return ''.join(new_board)


def visit_next_node(__open_list, __closed_list, __search_list):
    __visited_node = __search_list.pop()
    __open_list.remove(__visited_node)
    __closed_list.append(__visited_node)
    print("Visit node", __visited_node)

    # Goal state
    if __visited_node.find("1") == -1:
        print("Solution found")
        print("Search path (" + str(len(__closed_list)) + ")", __closed_list)
        __search_list = []
        return 1
    return __visited_node


closed_list = []
open_list = []
search_list = []
solution_path = []

# Initial board set up
n = 2
initial_board = "0110"

# n = 3
# initial_board = "011100010"

max_depth = 4
current_depth = 1
open_list.append(initial_board)
search_list.append(initial_board)

solved = False

# TODO Position conversion given an index
# TODO Max depth
# TODO File output
# TODO Tie breaking
while not len(search_list) == 0 and not solved:
    visited_node = visit_next_node(open_list, closed_list, search_list)
    if visited_node == 1:
        solved = True
        break
    create_child_nodes(visited_node, open_list, closed_list, search_list)
    print("Closed list (" + str(len(closed_list)) + ")", closed_list)
    print("Open list (" + str(len(open_list)) + ")", open_list)
    print("Search list (" + str(len(search_list)) + ")", search_list)
    print()
    # current_depth += 1

if len(search_list) == 0 and not solved:
    print("No solution")

