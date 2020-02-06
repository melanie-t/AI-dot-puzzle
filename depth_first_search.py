import math


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


def create_child_nodes(initial_node, open_list, closed_list, search_list, depth_list, current_depth):
    # Creates children of the initial
    print("Generated child nodes for ", initial_node)
    for token in range(0, len(initial_node)):
        child_node = flip_adjacent_nodes(initial_node, token)
        # Check to see if the node exists already
        node_exists = child_node in open_list or child_node in closed_list
        if not node_exists:
            # Add the child node to the open list and pop into search list stack
            print("\t\tDiscovered", child_node)
            depth_list[child_node] = current_depth
            open_list.append(child_node)
            search_list.append(child_node)
        elif child_node in open_list:
            # Node exists, update depth if new child node is lower
            if depth_list[child_node] > current_depth:
                print(child_node, "*** updated depth from", depth_list[child_node, "to", current_depth])
                depth_list[child_node] = current_depth


def visit_next_node(open_list, closed_list, search_list, depth_list, current_depth, max_depth):
    visited_node = search_list.pop()
    open_list.remove(visited_node)
    updated_depth = depth_list.pop(visited_node)
    # If the child node is not at max depth, then add to closed_list (meaning the node was expanded already)
    if not current_depth == max_depth:
        closed_list.append(visited_node)
    print("Visit node", visited_node, "| Depth: ", updated_depth)

    # Goal state
    if visited_node.find("1") == -1:
        print("Solution found")
        print("Search path (" + str(len(closed_list)) + ")", closed_list)
        __search_list = []
        return [visited_node, -1]

    return [visited_node, updated_depth]


def main():
    depth_list = dict()
    closed_list = []
    open_list = []
    search_list = []
    solution_path = []

    # Initial board set up
    n = 2
    initial_board = "0110"

    n = 3
    initial_board = "011100010"

    current_depth = 1
    max_depth = 5
    open_list.append(initial_board)
    search_list.append(initial_board)
    depth_list[initial_board] = 1
    solved = False

    # TODO File output
    # TODO Tie breaking
    while not len(search_list) == 0 and not solved:
        visited_node = visit_next_node(open_list, closed_list, search_list, depth_list, current_depth, max_depth)
        current_depth = visited_node[1]
        if visited_node[1] == -1:
            solved = True
            break

        if current_depth < max_depth:
            # Update the current_depth since we have made child_nodes
            current_depth += 1
            create_child_nodes(visited_node[0], open_list, closed_list, search_list, depth_list, current_depth)
            print("Updated depth:", current_depth)
            print("Closed list (" + str(len(closed_list)) + ")", closed_list)
            print("Open list (" + str(len(open_list)) + ")", open_list)
            print("Search list (" + str(len(search_list)) + ")", search_list)
            print("Depth list (" + str(len(depth_list)) + ")", depth_list)
            print()
        else:
            print("\tMAX DEPTH\n")
        # current_depth += 1

    if len(search_list) == 0 and not solved:
        print("No solution")


if __name__ == '__main__':
    main()

