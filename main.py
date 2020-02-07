import depth_first_search
import read_puzzle_file

# TODO @Patrick, remove these comments below when you're done with input file
# n = 3
# max_d = 100
# puzzle = "111001011"
# puzzle_name = "puzzle_1"

puzzles = [[3, 100, 111001011]]

# Initialize variables
for i in range(0, len(puzzles)):
    n = int(puzzles[i][0])
    max_d = int(puzzles[i][1])
    puzzle = str(puzzles[i][2])
    puzzle_name = "puzzle_" + str(i+1)

    depth_first_search.search(n, max_d, puzzle, puzzle_name)

