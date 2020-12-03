from math import prod

input_file = open("input", "r")
map_of_trees = [row.replace("\n", "") for row in input_file.readlines()]
input_file.close()

ROWS = len(map_of_trees)
COLUMNS = len(map_of_trees[0])


def count_trees(slope):
    position = [0, 0]

    tree_count = 0

    while position[0] < ROWS-1:
        position[0] += slope[0]
        position[1] = (position[1] + slope[1]) % COLUMNS
        if map_of_trees[position[0]][position[1]] == "#":
            tree_count += 1

    return tree_count


def main():
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    return prod(map(count_trees, slopes))


if __name__ == '__main__':
    print(main())
