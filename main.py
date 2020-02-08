import depth_first_search

# TODO @Patrick, remove these comments below when you're done with input file
# Replace puzzles with input puzzles from file
# Be careful with the initial board, it must be a string (or else 0001 becomes 1 as a number)
# puzzles = array of [n, max_d, initial_puzzle]
puzzles = []

game_file = open('input/games.txt')
# use readline() to read the first line
for line in game_file:
    game_info = line.replace("\n", "").split(" ")
    puzzles.append(game_info)
game_file.close()

# Initialize variables
for i in range(0, len(puzzles)):
    n = int(puzzles[i][0])
    max_d = int(puzzles[i][1])
    puzzle = str(puzzles[i][3])
    puzzle_name = "puzzle_" + str(i+1)

    depth_first_search.search(n, max_d, puzzle, puzzle_name)

