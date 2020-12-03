input_file = open("input", "r")
map_of_trees = [row.replace("\n", "") for row in input_file.readlines()]
input_file.close()

ROWS = len(map_of_trees)
COLUMNS = len(map_of_trees[0])


def main():
    slope = (1, 3)
    position = [0, 0]

    tree_count = 0

    while position[0] < ROWS-1:
        position[0] += slope[0]
        position[1] = (position[1] + slope[1]) % COLUMNS
        if map_of_trees[position[0]][position[1]] == "#":
            tree_count += 1
    return tree_count


if __name__ == '__main__':
    print(main())
