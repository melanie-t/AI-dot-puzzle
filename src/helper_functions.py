# Helper functions to manipulate nodes
import os
import errno
from collections import deque
from src.enum_classes import MovesList, OutputValues


def position(index, size_n):
    # A starts at 65
    letter = chr(65 + int(index / size_n))
    n_pos = int(index % size_n + 1)
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


def create_solution_path(initial_puzzle, solution_node, node_info_list):
    solution_path = deque()
    current_move = solution_node
    current_position = node_info_list[solution_node][MovesList.POSITION]
    while current_move != initial_puzzle:
        solution_path.appendleft([current_position, current_move])
        current_position = node_info_list[current_move][MovesList.POSITION]
        current_move = node_info_list[current_move][MovesList.PARENT_NODE]
    solution_path.appendleft([node_info_list[initial_puzzle][MovesList.PARENT_NODE], initial_puzzle])
    return solution_path


# Source: https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory/14364249#14364249
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
# End source


def create_output_files(solved, search_path, solution_path, puzzle_num, search_type):
    make_sure_path_exists("./output/")
    solution_output_path = "./output/" + str(puzzle_num) + "_" + search_type + "_solution.txt"
    search_output_path = "./output/" + str(puzzle_num) + "_" + search_type + "_search.txt"
    # Save search path
    try:
        f_search = open(search_output_path, "w")
        for node in search_path:
            output_values = node[0]
            node_value = node[1]
            f_search.write(f"{output_values[OutputValues.F_N]} "
                           f"{output_values[OutputValues.G_N]} "
                           f"{output_values[OutputValues.H_N]} "
                           f"{node_value} \n")
        # print("\tSaved search path at", search_output_path)
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
        # print("\tSaved solution at", solution_output_path)
    except IOError:
        print("Other unspecified IO error")
    except:
        print("Unknown error")
    else:
        f_solution.close()


def save_solution(search_path, moves_list, puzzle, puzzle_num, search_type, solution_node, solved):
    solution_path = []
    if solved:
        solution_path = create_solution_path(puzzle, solution_node, moves_list)
        print(f"[ {search_type} ][ Solution Found ]")

        print(f"\tSearch path ({len(search_path)}) {search_path[:20]} ... "
              f"\n"
              f"\tSolution path ({len(solution_path)}) {solution_path}")

    else:
        print(f"[ {search_type} ][ No Solution ]")
        print(f"\tSearch path ({len(search_path)})"
              f"\n"
              f"\tSolution path ({len(solution_path)})")

    # Save output file
    create_output_files(solved, search_path, solution_path, puzzle_num, search_type)
