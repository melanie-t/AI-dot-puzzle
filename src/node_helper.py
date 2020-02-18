# Helper functions to manipulate nodes
import os
import errno
from collections import deque
from src.enum_node_info import NodeInfo


# Source: https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory/14364249#14364249
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
# End source


def save_output_files(solved, search_path, solution_path, puzzle_name):
    make_sure_path_exists("./output/")
    solution_output_path = "./output/" + puzzle_name + "solution.txt"
    search_output_path = "./output/" + puzzle_name + "search.txt"
    # Save search path
    try:
        f_search = open(search_output_path, "w")
        if solved:
            for node in search_path:
                f_search.write("0 0 0 " + node + "\n")
        else:
            f_search.write("No solution")
        print("Saved search path at", search_output_path)
    except IOError:
        print("Other unspecified IO error")
    except:
        print("Unknown error")
    else:
        f_search.close()

    # Save solution path
    try:
        f_solution = open(solution_output_path, "w")
        if solved:
            for node in solution_path:
                f_solution.write(str(node[0]) + " " + str(node[1]) + "\n")
        else:
            f_solution.write("No solution")
        print("Saved solution at", solution_output_path)
    except IOError:
        print("Other unspecified IO error")
    except:
        print("Unknown error")
    else:
        f_solution.close()


def position(index, n):
    # A starts at 65
    letter = chr(65 + int(index/n))
    n_pos = int(index % n + 1)
    current_position = letter + str(n_pos)
    return current_position


def flip_token(token):
    if token == '0':
        return '1'
    else:
        return '0'


def flip_adjacent_nodes(board, index, size_n):
    # Copy the board to modify the new board
    new_board = list(board)
    max_index = size_n - 1
    token_above = index - size_n
    token_below = index + size_n
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
    elif index == size_n*max_index:
        new_board[index] = flip_token(new_board[index])
        new_board[token_above] = flip_token(new_board[token_above])
        new_board[token_right] = flip_token(new_board[token_right])

    # Bottom right Corner
    elif index == size_n*size_n-1:
        new_board[index] = flip_token(new_board[index])
        new_board[token_above] = flip_token(new_board[token_above])
        new_board[token_left] = flip_token(new_board[token_left])

    # Left edge
    elif index % size_n == 0:
        new_board[index] = flip_token(new_board[index])
        new_board[token_above] = flip_token(new_board[token_above])
        new_board[token_below] = flip_token(new_board[token_below])
        new_board[token_right] = flip_token(new_board[token_right])

    # Right edge
    elif (index+1) % size_n == 0:
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
    elif int(index / size_n) == max_index:
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


def create_child_nodes(initial_node, open_list, moves_list, current_depth, size_n):
    # Creates children of the initial
    sorted_children = []
    for token in range(0, len(initial_node)):
        child_node = flip_adjacent_nodes(initial_node, token, size_n)
        # Check to see if the node exists already
        new_node = child_node not in moves_list
        if new_node:
            # Add the child node to the open list and pop into search list stack
            moves_list[child_node] = [current_depth, position(token, size_n), initial_node]
            sorted_children.append(child_node)
        else:
            # Node exists, update depth if new child node is lower
            node_depth = (moves_list[child_node][NodeInfo.G_N.value])
            if node_depth > current_depth:
                moves_list[child_node] = [current_depth, position(token, size_n), initial_node]
    # Tie breaker by sorting the children
    # Reverse order sorting because we are using a stack, the last element should be the next node
    sorted_children.sort(reverse=True)
    open_list.extend(sorted_children)


def visit_next_node(solution_node, open_list, closed_list, moves_list, search_path, current_depth, max_depth):
    visited_node = open_list.pop()
    node_info = moves_list[visited_node]
    search_path.append(visited_node)
    # If the child node is not at max depth, then add to closed_list (meaning the node was expanded already)
    if not current_depth == max_depth:
        closed_list.append(visited_node)

    # Goal state
    if visited_node == solution_node:
        closed_list.append(visited_node)
        open_list.clear()   # clear for the stopping condition when open_list length is 0
        return [visited_node, [-1, '0']]

    return [visited_node, node_info]


def create_solution_path(initial_puzzle, solution_node, moves_list):
    solution_path = deque()
    current_move = solution_node
    current_position = moves_list[solution_node][NodeInfo.POSITION.value]
    while current_move != initial_puzzle:
        solution_path.appendleft([current_position, current_move])
        current_position = moves_list[current_move][NodeInfo.POSITION.value]
        current_move = moves_list[current_move][NodeInfo.PARENT_NODE.value]
    solution_path.appendleft([moves_list[initial_puzzle][NodeInfo.PARENT_NODE.value], initial_puzzle])
    return solution_path
