from src import depth_first_search, informed_search


def file_read(path, puzzles):
    try:
        game_file = open(path)
        # use readline() to read the first line
        for line in game_file:
            game_info = line.replace("\n", "").split(" ")
            puzzles.append(game_info)
    except FileNotFoundError:
        print("Unable to find game info file. Make sure the path is correct")
    except IOError:
        print("Other unspecified IO error")
    except:
        print("Unknown error")
    else:
        game_file.close()


def main():
    print("================================================")
    print("||  Welcome to A* Is Born's Search Algorithm  ||")
    print("================================================")

    puzzles = []  # Puzzles specified outside to keep all games separate
    while True:
        print("\nInput quit to terminate the application")
        user_input = str(input("Enter the path of game info text file (ex: input/games.txt): "))
        if user_input == "quit":
            break
        else:
            file_read(user_input, puzzles)
        # Initialize variables
        for i in range(0, len(puzzles)):
            n = int(puzzles[i][0])
            max_d = int(puzzles[i][1])
            max_l = int(puzzles[i][2])
            puzzle = str(puzzles[i][3])
            puzzle_num = str(i + 1)
            print_steps_enabled = False  # False for faster run time

            print()
            print(n, max_d, max_l, puzzle)

            # Depth First Search
            #depth_first_search.search(size_n=n, max_d=max_d, puzzle=puzzle, puzzle_num=puzzle_num, print_steps_enabled=print_steps_enabled)

            # Best First Search
            informed_search.search(size_n=n, max_l=max_l, puzzle=puzzle, puzzle_num=puzzle_num,
                                   print_steps_enabled=print_steps_enabled, search_type="bfs")

            # A* Search
            informed_search.search(size_n=n, max_l=max_l, puzzle=puzzle, puzzle_num=puzzle_num,
                                   print_steps_enabled=print_steps_enabled, search_type="astar")


if __name__ == '__main__':
    main()