from collections import deque


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


def create_child_nodes(initial_node, open_list, closed_list, moves_list, current_depth, size_n):
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
            node_depth = (moves_list[child_node][0])
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
    current_position = moves_list[solution_node][1]
    while current_move != initial_puzzle:
        solution_path.appendleft([current_position, current_move])
        current_position = moves_list[current_move][1]
        current_move = moves_list[current_move][2]
    solution_path.appendleft([moves_list[initial_puzzle][2],initial_puzzle])
    return solution_path


def search(size_n, max_d, puzzle, puzzle_name, print_steps_enabled):
    moves_list = dict()
    closed_list = []
    open_list = []
    search_path = []

    current_depth = 1
    open_list.append(puzzle)
    search_path.append(puzzle)
    moves_list[puzzle] = [1, 0, 0]
    solution_node = (size_n*size_n)*'0'
    solved = False

    while not len(open_list) == 0 and not solved:
        # Visit node
        visited_node = visit_next_node(solution_node, open_list, closed_list, moves_list, search_path, current_depth, max_d)
        current_depth = (visited_node[1])[0]

        if print_steps_enabled:
            current_board_position = visited_node[0]
            node_info = visited_node[1]
            print("Visit node", current_board_position, "| Move:", node_info[1], "| Depth:", node_info[0])


        # Check if the goal state is returned
        if current_depth == -1:
            solved = True
            break

        if current_depth < max_d:
            # Update the current_depth since we have generated child_nodes
            current_depth += 1
            # Generate children nodes, sort the children nodes and add to the open list
            create_child_nodes(visited_node[0], open_list, closed_list, moves_list, current_depth, size_n)
            if print_steps_enabled:
                print("\tGenerating children for node", visited_node[0], "\n")
                print("Closed list (" + str(len(closed_list)) + ")", closed_list)
                print("Open list (" + str(len(open_list)) + ")", open_list)
                print("Moves list (" + str(len(moves_list)) + ")", moves_list)
                print("Search path (" + str(len(search_path)) + ")", search_path)
                print()

    # No solution or solution found
    if len(open_list) == 0:
        solution_output_path = "./output/" + str(puzzle_name) + "_dfs_solution.txt"
        search_output_path = "./output/" + str(puzzle_name) + "_dfs_search.txt"
        if solved:
            solution_path = create_solution_path(puzzle, solution_node, moves_list)
            print(puzzle_name, ": Solution found")
            if print_steps_enabled:
                print("Search path (" + str(len(search_path)) + ") saved at", search_output_path, search_path)
                print("Solution path (" + str((len(solution_path))) + ") saved at", solution_output_path, solution_path)
            else:
                print("Search path (" + str(len(search_path)) + ") saved at", search_output_path)
                print("Solution path (" + str((len(solution_path))) + ") saved at", solution_output_path)

        else:
            print(puzzle_name, ": No solution")

        # Save search path
        try:
            f_search = open(search_output_path, "w")
            if solved:
                for node in search_path:
                    f_search.write("0 0 0 "+node+"\n")
            else:
                f_search.write("No solution")
        except IOError:
            print("Other unspecified IO error")
        except:
            print("Unknown error")
        finally:
            f_search.close()

        # Save solution path
        try:
            f_solution = open(solution_output_path, "w")
            if solved:
                for node in solution_path:
                    f_solution.write(str(node[0]) + " " + str(node[1]) + "\n")
            else:
                f_solution.write("No solution")
        except IOError:
            print("Other unspecified IO error")
        except:
            print("Unknown error")
        finally:
            f_solution.close()