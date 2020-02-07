import math

# TODO File output
# TODO Solution path
# TODO Read file and input into variables


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


def create_child_nodes(initial_node, open_list, closed_list, moves_dict, current_depth):
    # Creates children of the initial
    print("Generated child nodes for ", initial_node)
    sorted_children = []
    for token in range(0, len(initial_node)):
        child_node = flip_adjacent_nodes(initial_node, token)
        # Check to see if the node exists already
        node_exists = child_node in open_list or child_node in closed_list
        if not node_exists:
            # Add the child node to the open list and pop into search list stack
            print("\t\tDiscovered", child_node)
            moves_dict[child_node] = [current_depth, position(token, math.sqrt(len(initial_node)))]
            sorted_children.append(child_node)
        elif child_node in open_list:
            node_depth = (moves_dict[child_node][0])
            # Node exists, update depth if new child node is lower
            if node_depth > current_depth:
                print(child_node, "*** updated depth from", moves_dict[child_node, "to", current_depth])
                moves_dict[child_node] = [current_depth, str(position(int(token)))]
    # Tie breaker by sorting the children
    # Reverse order sorting because we are using a stack, the last element should be the next node
    sorted_children.sort(reverse=True)
    open_list.extend(sorted_children)


def visit_next_node(open_list, closed_list, moves_dict, search_path, current_depth, max_depth):
    visited_node = open_list.pop()
    updated_depth = moves_dict.pop(visited_node)
    search_path.append(visited_node)
    # If the child node is not at max depth, then add to closed_list (meaning the node was expanded already)
    if not current_depth == max_depth:
        closed_list.append(visited_node)
    print("Visit node", visited_node, "| Depth: ", updated_depth)

    # Goal state
    if visited_node.find("1") == -1:
        closed_list.append(visited_node)
        open_list.clear()   # clear for the stopping condition when open_list length is 0
        return [visited_node, [-1, '0']]

    return [visited_node, updated_depth]


def main():
    moves_dict = dict()
    closed_list = []
    open_list = []
    search_path = []
    solution_path = []

    # Initial board set up
    n = 2
    initial_board = "0110"

    n = 3
    max_d = 20
    initial_board = "111001011"

    current_depth = 1
    open_list.append(initial_board)
    search_path.append(initial_board)
    moves_dict[initial_board] = [1, 0]
    solved = False

    while not len(open_list) == 0 and not solved:
        # Visit node
        visited_node = visit_next_node(open_list, closed_list, moves_dict, search_path, current_depth, max_d)
        current_depth = (visited_node[1])[0]
        # Check if the goal state is returned
        if current_depth == -1:
            solved = True
            break

        if current_depth < max_d:
            # Update the current_depth since we have generated child_nodes
            current_depth += 1
            # Generate children nodes, sort the children nodes and add to the open list
            create_child_nodes(visited_node[0], open_list, closed_list, moves_dict, current_depth)
            print("Updated depth:", current_depth)
            print("Closed list (" + str(len(closed_list)) + ")", closed_list)
            print("Open list (" + str(len(open_list)) + ")", open_list)
            print("Moves list (" + str(len(moves_dict)) + ")", moves_dict)
            print("Search path (" + str(len(search_path)) + ")", search_path)
            print()
        else:
            print("\tMAX DEPTH\n")

    if len(open_list) == 0:
        if solved:
            print("Solution found")
            print("Search path (" + str(len(search_path)) + ")", search_path)
            print("Solution path(" + str((len(solution_path))) + ")", solution_path)
        else:
            print("No solution")


if __name__ == '__main__':
    main()

