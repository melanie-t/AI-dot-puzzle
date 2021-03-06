from bisect import insort
from collections import deque
from src.heuristics import calculate_heuristics
from src.helper_functions import flip_adjacent_nodes, position, save_solution
from src.enum_classes import MovesList, OpenList, VisitedNode
import itertools


def search(size_n, max_l, puzzle, puzzle_num, print_steps_enabled, search_type, heuristic_num):
    # moves_list is a list with [f(n), g(n), h(n), position, parent_node]
    # Keeps track of all the moves discovered
    # Enum class MovesList will be used to access indices
    moves_list = dict()

    # open_list is a sorted list containing the nodes to visit with the structure [f(n), node]
    # Enum class OpenList will be used to access indices
    open_list = deque()

    # search_path contains all the nodes checked for goal state
    search_path = []

    # Initialize the puzzle with initial board node
    node = puzzle
    g_n = 0
    h_n = 0
    f_n = 0
    move_position = 0
    parent_node = 0

    # Initialize moves_list, open_list and search_path with the puzzle
    moves_list[node] = [f_n, g_n, h_n, move_position, parent_node]
    open_list.append([f_n, node])

    solution_node = (size_n * size_n) * '0'  # Solution node
    solved = False

    while not len(open_list) == 0 and not solved and len(search_path) < max_l:
        # visited_node has the value [node, moves_list[node]]
        visited_node = visit_next_node(solution_node, open_list, moves_list, search_path)

        current_node = visited_node[VisitedNode.NODE]
        node_info = visited_node[VisitedNode.NODE_INFO]

        if print_steps_enabled:
            f_n = node_info[MovesList.F_N]
            g_n = node_info[MovesList.G_N]
            h_n = node_info[MovesList.H_N]
            move_position = node_info[MovesList.POSITION]
            parent = node_info[MovesList.PARENT_NODE]
            print(f"Visited node {current_node}"
                  f"\t f(n): {f_n} "
                  f"\t g(n): {g_n} "
                  f"\t h(n): {h_n} "
                  f"\t Position: {move_position}"
                  f"\t Parent: {parent}"
                  )

        # Check if the solution was found
        if visited_node[VisitedNode.SOLVED] == 1:
            solved = True
            break

        # Continue looking for a solution
        # Create children nodes if the solution hasn't been found yet and the search_path max length hasn't been reached
        if len(search_path) < max_l:
            create_child_nodes(current_node, open_list, moves_list, size_n, search_type, heuristic_num)
            if print_steps_enabled:
                print(f"\tGenerating children for node {current_node}"
                      f"\n\tMoves list ({len(moves_list)}) {list(itertools.islice(moves_list, 0, 20))} ... "
                      f"\n\tOpen list ({len(open_list)}) {list(itertools.islice(open_list, 0, 20))} ... "
                      f"\n\tSearch path ({len(search_path)}) {search_path[:20]}) ... "
                      f"\n")

    save_solution(search_path, moves_list, puzzle, puzzle_num, search_type, solution_node, solved, print_steps_enabled)


# Function visit_next_node
# Checks if the first node in the open_list is the goal state
# Updates the open_list, closed_list, search_path
# Returns the node visited, the node_info and 0 or 1 if it's solved
def visit_next_node(solution_node, open_list, moves_list, search_path):
    visited_node = open_list.popleft()
    board_node = visited_node[OpenList.NODE]

    node_info = moves_list[board_node]

    g_n = node_info[MovesList.G_N]
    h_n = node_info[MovesList.H_N]
    f_n = node_info[MovesList.F_N]

    search_path.append(([f_n, g_n, h_n], board_node))

    # The node is the goal state
    if board_node == solution_node:
        open_list.clear()   # clear for the stopping condition when open_list length is 0
        parent_position = node_info[MovesList.POSITION]
        return [board_node, node_info, 1]
    return [board_node, node_info, 0]


# Function create_child_nodes generates the child nodes given a board configuration
# It will also calculate the g(n), h(n) and f(n)
def create_child_nodes(initial_node, open_list, moves_list, size_n, search_type, heuristic_num):
    parent_depth = moves_list[initial_node][MovesList.G_N]
    child_depth = parent_depth + 1

    for token in range(0, len(initial_node)):
        child_node = flip_adjacent_nodes(initial_node, token, size_n)
        g_n = 0
        if search_type == "astar":
            g_n = child_depth
        h_n = calculate_heuristics(child_node, heuristic_num)
        f_n = g_n + h_n

        # Check to see if the node exists already
        if child_node not in moves_list:
            # Add the child node to the children list
            moves_list[child_node] = [f_n, g_n, h_n, position(token, size_n), initial_node]

            # To ensure the lowest heuristic goes first, we sort the children by f(n)
            # The tie breaker is implemented by sort as well, as the first white node will show as sorted
            insort(open_list, [f_n, child_node])

        else:   # Node exists
            existing_node_info = moves_list[child_node]
            existing_node_f_n = existing_node_info[MovesList.F_N]

            # Update depth g(n) if the new child depth is lower
            # Removes the old child node and inserts the new node with updated g(n)
            if f_n < existing_node_f_n:
                # Update existing node with new values
                moves_list[child_node] = [f_n, g_n, h_n, position(token, size_n), initial_node]

                # Remove old child node from the open list
                if [existing_node_f_n, child_node] in open_list:
                    open_list.remove([existing_node_f_n, child_node])

                # Insert the new child node with correct f_n value
                insort(open_list, [f_n, child_node])
