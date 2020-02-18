from src.enum_node_info import NodeInfo
from src.node_helper import create_child_nodes, visit_next_node, create_solution_path, save_output_files


def search(size_n, max_d, puzzle, puzzle_num, print_steps_enabled):
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
            print("Visit node", current_board_position,
                  "| Move:", node_info[NodeInfo.POSITION.value],
                  "| Depth:", node_info[NodeInfo.G_N.value])

        # Check if the goal state is returned
        if current_depth == -1:
            solved = True
            break

        if current_depth < max_d:
            # Update the current_depth since we have generated child_nodes
            current_depth += 1
            # Generate children nodes, sort the children nodes and add to the open list
            create_child_nodes(visited_node[0], open_list, moves_list, current_depth, size_n)
            if print_steps_enabled:
                print("\tGenerating children for node", visited_node[0], "\n")
                print("Closed list (" + str(len(closed_list)) + ")", closed_list)
                print("Open list (" + str(len(open_list)) + ")", open_list)
                print("Moves list (" + str(len(moves_list)) + ")", moves_list)
                print("Search path (" + str(len(search_path)) + ")", search_path)
                print()

    # No solution or solution found
    if len(open_list) == 0:
        if solved:
            solution_path = create_solution_path(puzzle, solution_node, moves_list)
            print("Puzzle", puzzle_num, ": Solution found")
            if print_steps_enabled:
                print("Search path (" + str(len(search_path)) + ")", search_path)
                print("Solution path (" + str((len(solution_path))) + ")", solution_path)
            else:
                print("Search path (" + str(len(search_path)) + ")")
                print("Solution path (" + str((len(solution_path))) + ")")
        else:
            print(puzzle_num, ": No solution")

        # Save output file
        save_output_files(solved, search_path, solution_path, puzzle_num + "_dfs_")

