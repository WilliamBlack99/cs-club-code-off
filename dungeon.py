from random import randint

# for printing rows like this: +---+---+---+
def print_row_type_1(column_num):
    for j in range(column_num):
        if j == 0:
            print("+", end="")
        print("---+", end="")
    print()

# for printing rows like this: |   |   |   |
def print_row_type_2(column_num):
    for j in range(column_num):
        if j == 0:
            print("|", end="")
        print("   |", end="")
    print()

# for printing rows like this: | 15|-11|  4|
def print_row_type_3(dungeon, row_index):
    for i in range(len(dungeon)):
        if i == 0:
            print("|", end="")
        if len(str(dungeon[i][row_index])) == 1:
            print("  ", end="")
        elif len(str(dungeon[i][row_index])) == 2:
            print(" ", end="")
        print(dungeon[i][row_index], end="")
        print("|", end="")
    print()

# print the map of the dungeon
def print_dungeon(dungeon):
    for i in range(len(dungeon[0])):
        print_row_type_1(len(dungeon))
        print_row_type_2(len(dungeon))
        print_row_type_3(dungeon, i)
        print_row_type_2(len(dungeon))
    print_row_type_1(len(dungeon))


# generate a width x height matrix of random integers to be the dungeon map
def generate_dungeon(width, height):
    dungeon = []
    for column in range(width):
        column = []
        for row in range(height):
            column.append(randint(-20, 10))
        dungeon.append(column)

    return dungeon


def find_best_paths(dungeon):
    # dungeon = [[-2, -5, 10], [-3, -10, 30], [3, 1, -5]]

    # recursive function that finds all p=valid paths starting at a specific health
    def health_from_paths(x, y, health, path, dungeon_map):
        # modify the current health by the amount in this room of the dungeon
        health += dungeon_map[x][y]

        # if the hero is dead, end recursion. a path was not found
        if health <= 0:
            return []

        # if the hero is in the bottom right, end recursion. a path was found
        if x == len(dungeon_map) - 1 and y == len(dungeon_map[x]) - 1:
            return [path]

        # begin recursion by checking right and down of the current space
        paths = []
        if x + 1 < len(dungeon_map):
            paths += health_from_paths(x + 1, y, health, path + ['right'], dungeon_map)
        if y + 1 < len(dungeon_map[x]):
            paths += health_from_paths(x, y + 1, health, path + ['down'], dungeon_map)

        return paths

    # increment the starting health until there is a valid path(s)
    path_found = False  # flag variable
    starting_health = 0
    while not path_found:
        starting_health += 1
        valid_paths = health_from_paths(0, 0, starting_health, [], dungeon)
        if valid_paths:
            path_found = True

    return valid_paths, starting_health
