import alphabet, duplication, numerals, sudoku, dungeon

if __name__ == '__main__':
    # alphabet sorting
    print("Challenge #1: Sort a string alphabetically")
    in_string = input("Enter a string: ")
    print(alphabet.sort(in_string))

    # roman numerals
    print("\nChallenge #2: Find the value of roman numerals")
    user_input = input("Enter roman numerals: ")
    value = numerals.convert_numerals(user_input)
    if value:
        print("The value of the roman numerals is", value)
    else:
        print("Not all input numerals were roman numerals")

    # list duplication
    print("\nChallenge #3: Find the most duplicates")

    # take the user input and turn it into a list
    user_input = input("Enter a list of numbers separated by spaces: ")
    in_list = user_input.split()

    # get the maximum value and the number of repetitions it has
    repetitions, maximum = duplication.find_duplicates(in_list)

    # print results
    if maximum:
        print("The value repeated the most is", maximum)
        print("It was repeated", repetitions, "times")
    else:
        print("There is not a value that occurs the most")

    # dungeon
    print("\nChallenge #4: Find the best path through the dungeon")
    width = input("What is the width of the dungeon?\n")
    height = input("What is the height of the dungeon?\n")
    try:
        width = int(width)
        height = int(height)
    except ValueError:
        print("The width and height must be integers")
    dungeon_map = dungeon.generate_dungeon(width, height)
    dungeon.print_dungeon(dungeon_map)
    paths, health = dungeon.find_best_paths(dungeon_map)
    if len(paths) > 1:
        print("The best paths through the dungeon are:")
        for path in paths:
            print(", ".join(path))
    else:
        print("The best path through the dungon is:")
        print(", ".join(paths[0]))
    print("The minimum health needed is", health)


    # sudoku
    print("\nChallenge #5: Is a sudoku board valid?")
    file_name = input("What is the full name of the sudoku board file? (with extension)\n")
    if sudoku.is_valid(file_name):
        print("The sudoku board is valid")
    else:
        print("The sudoku board is not valid")