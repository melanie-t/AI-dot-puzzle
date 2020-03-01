from src.enum_classes import MovesList, VisitedNode
from src.helper_functions import save_solution, flip_adjacent_nodes, position


def search(size_n, max_d, puzzle, puzzle_num, print_steps_enabled):
    node_info_list = dict()
    closed_list = []
    open_list = []
    search_path = []

    current_depth = 0
    open_list.append(puzzle)
    search_path.append([[0, 0, 0], puzzle])
    node_info_list[puzzle] = [0, 1, 0, 0, 0]
    solution_node = (size_n*size_n)*'0'
    solved = False

    while not len(open_list) == 0 and not solved:
        # Visit node
        visited_node = visit_next_node(solution_node, open_list, closed_list, node_info_list, search_path, current_depth, max_d)
        current_node = visited_node[VisitedNode.NODE]
        node_info = visited_node[VisitedNode.NODE_INFO]
        current_depth = node_info[MovesList.G_N]

        if print_steps_enabled:
            print("Visit node", current_node,
                  "| Move:", node_info[MovesList.POSITION],
                  "| Depth:", node_info[MovesList.G_N])

        # Check if the goal state is returned
        if current_depth == -1:
            solved = True
            break

        if current_depth < max_d:
            # Update the current_depth since we have generated child_nodes
            current_depth += 1
            # Generate children nodes, sort the children nodes and add to the open list
            create_child_nodes(visited_node[0], open_list, node_info_list, current_depth, size_n)
            if print_steps_enabled:
                print("\tGenerating children for node", visited_node[0], "\n")
                print("Closed list (" + str(len(closed_list)) + ")", closed_list)
                print("Open list (" + str(len(open_list)) + ")", open_list)
                print("Moves list (" + str(len(node_info_list)) + ")", node_info_list)
                print("Search path (" + str(len(search_path)) + ")", search_path)
                print()

    save_solution(search_path, node_info_list, puzzle, puzzle_num, "dfs", solution_node, solved, print_steps_enabled)


def create_child_nodes(initial_node, open_list, node_info_list, current_depth, size_n):
    # Creates children of the initial
    sorted_children = []
    for token in range(0, len(initial_node)):
        child_node = flip_adjacent_nodes(initial_node, token, size_n)
        # Check to see if the node exists already
        new_node = child_node not in node_info_list
        if new_node:
            # Add the child node to the open list and pop into search list stack
            node_info_list[child_node] = [0, current_depth, 0, position(token, size_n), initial_node]
            sorted_children.append(child_node)
        else:
            # Node exists, update depth if new child node is lower
            node_depth = (node_info_list[child_node][MovesList.G_N])
            if node_depth > current_depth:
                node_info_list[child_node] = [0, current_depth, 0, position(token, size_n), initial_node]
    # Tie breaker by sorting the children
    # Reverse order sorting because we are using a stack, the last element should be the next node
    sorted_children.sort(reverse=True)
    open_list.extend(sorted_children)


def visit_next_node(solution_node, open_list, closed_list, moves_list, search_path, current_depth, max_depth):
    visited_node = open_list.pop()
    node_info = moves_list[visited_node]
    search_path.append([[0, 0, 0], visited_node])
    # If the child node is not at max depth, then add to closed_list (meaning the node was expanded already)
    if not current_depth == max_depth:
        closed_list.append(visited_node)

    # Goal state
    if visited_node == solution_node:
        closed_list.append(visited_node)
        open_list.clear()   # clear for the stopping condition when open_list length is 0
        return [visited_node, [0, -1, 0, '0'], 1]
    return [visited_node, node_info]