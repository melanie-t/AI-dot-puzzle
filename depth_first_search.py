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


def create_child_node(initial_node):
    print("Creating tree")
    # Creates children of the initial
    for i in initial_node:
        child_node = flip_adjacent_nodes(initial_node, i)
        g.add_node(child_node)
        g.link_parent_child(initial_node, child_node)
    # TODO Create not only for the initial node but for children of children of initial node
    # PB : when do i know when i can stop the loop


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


# TODO Implement txt file parser

# Example using flip_adjacent_nodes
# initial_board = "0000000000000000"
# new_board = flip_adjacent_nodes(initial_board, 4)
g = Graph()
