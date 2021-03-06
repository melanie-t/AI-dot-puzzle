from src import depth_first_search, informed_search
from src.helper_functions import file_read


def main():
    print("================================================")
    print("||  Welcome to A* Is Born's Search Algorithm  ||")
    print("================================================")

    puzzles = []  # Puzzles specified outside to keep all games separate
    heuristic_num = 0
    valid_path = False
    while True:
        print("\nInput quit to terminate the application")
        user_input = str(input("Enter the path of game info text file (ex: input/games.txt): "))
        if user_input == "quit":
            break
        else:
            valid_path = file_read(user_input, puzzles)

        if valid_path:
            while True:
                heuristic_num = str(input("Enter the heuristic number (1-3) to evaluate: "))
                if heuristic_num == '1' or heuristic_num == '2' or heuristic_num == '3' or heuristic_num == 'quit':
                    break
                else:
                    print("Invalid heuristic number, please select a heuristic from 1 to 3.")

            if heuristic_num == "quit":
                break

        # Initialize variables
        for i in range(0, len(puzzles)):
            n = int(puzzles[i][0])
            max_d = int(puzzles[i][1])
            max_l = int(puzzles[i][2])
            puzzle = str(puzzles[i][3])
            puzzle_num = str(i + 1)

            print()
            print(n, max_d, max_l, puzzle)

            # Depth First Search
            depth_first_search.search(size_n=n, max_d=max_d, puzzle=puzzle, puzzle_num=puzzle_num,
                                      print_steps_enabled=False)

            # Best First Search
            informed_search.search(size_n=n, max_l=max_l, puzzle=puzzle, puzzle_num=puzzle_num,
                                   print_steps_enabled=False, search_type="bfs", heuristic_num=heuristic_num)

            # A* Search
            # We print the steps for A* to be referred to in the demo explanation
            informed_search.search(size_n=n, max_l=max_l, puzzle=puzzle, puzzle_num=puzzle_num,
                                   print_steps_enabled=True, search_type="astar", heuristic_num=heuristic_num)


if __name__ == '__main__':
    main()