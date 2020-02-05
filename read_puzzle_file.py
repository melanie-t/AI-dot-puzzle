#contains each row in the puzzle text file. Replace sample_puzzle with the actual file name
gameline = []

#empty board
the_board = []

#reading the entire file and putting it into an array of gameline
with open('sample_puzzles.txt', 'r') as file:
    for count, line in enumerate(file):
        gameline.append(line)

#to select the different boards, just change gameline's index.
#ex: gameline[0], gameline[1], etc...

#>>beginning of loop can start here

#strip the info from the gameline's array and store it in each individual component
game_info = gameline[0].split()

#test print
print(game_info)

#game_info[0] is the board's n*n dimension
dimension = int(game_info[0])
print(dimension)

#game_info[1] is the max depth
max_depth = int(game_info[1])
print(max_depth)

#game_info[2] is the max search path length
dfs_max_depth = int(game_info[2])
print(dfs_max_depth)

#game_info[3] is the board's setup w/ the pieces
bfs_max_path_length = int(game_info[3])
print(bfs_max_path_length)

#convert entire string component into int array
for piece in game_info[3]:
    the_board.append(int(piece))

print(the_board)

#>>after every game has been tested with our BFS and DFS
#>>end of loop for the program can finish here