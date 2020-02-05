import math


class Node:
    def __init__(self, node):
        self.id = node
        self.child_node = {}  # Dictionary containing children

    def add_child(self, child):
        self.child_node[child] = 1  # Each node children weight is 1

    def get_id(self):
        return self.id  # Can be useful...


class Graph:
    def __init__(self):
        self.node_dict = {}  # Dictionary containig nodes
        self.nb_nodes = 0

    def add_node(self, node):
        self.nb_nodes += 1
        new_node = Node(node)
        self.node_dict[node] = new_node
        return new_node

    def link_parent_child(self, parent, child):
        # If child node does not exist create it
        if child not in self.node_dict:
            self.add_node(child)
        self.node_dict[parent].add_child(self.node_dict[child])

# TODO Remove?
# def create_child_node(initial_node):
#     print("Creating tree")
#     # Creates children of the initial
#     for i in initial_node:
#         child_node = flip_adjacent_nodes(initial_node, i)
#         g.add_node(child_node)
#         g.link_parent_child(initial_node, child_node)
#     # PB : when do i know when i can stop the loop


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


def visit_next_node(__open_list, __closed_list, __search_list, __search_path):
    __visited_node = __search_list.pop()
    __search_path.append(__visited_node)
    print("Visit node", __visited_node)

    __open_list.remove(__visited_node)
    __closed_list.append(__visited_node)

    # Goal state
    if __visited_node.find("1") == -1:
        print("Solution found")
        print("Search path (" + str(len(__search_path)) + ")", __search_path)
        __search_list = []
        return 1
    return __visited_node


closed_list = []
open_list = []
search_list = []
search_path = []
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


