from copy import deepcopy
input_file = open("input", "r")
area_map = [[symbol for symbol in row.replace("\n", "")] for row in input_file.readlines()]
input_file.close()

ROWS = len(area_map)
COLUMNS = len(area_map[0])

buffer_area_map = deepcopy(area_map)


def get_occupied_direction_seats_number(row, column):
    number = direction_value(row, column, (-1, -1))
    number += direction_value(row, column, (-1, 0))
    number += direction_value(row, column, (-1, 1))
    number += direction_value(row, column, (0, -1))
    number += direction_value(row, column, (0, 1))
    number += direction_value(row, column, (1, -1))
    number += direction_value(row, column, (1, 0))
    number += direction_value(row, column, (1, 1))
    return number


def direction_value(i, j, direction):
    while True:
        i += direction[0]
        j += direction[1]
        if 0 <= i < ROWS:
            if 0 <= j < COLUMNS:
                if area_map[i][j] == "#":
                    return 1
                elif area_map[i][j] == "L":
                    return 0
            else:
                return 0
        else:
            return 0

change = True
while change:
    change = False
    for i in range(ROWS):
        for j in range(COLUMNS):
            if area_map[i][j] == "L" and get_occupied_direction_seats_number(i, j) == 0:
                buffer_area_map[i][j] = "#"
                change = True
            elif area_map[i][j] == "#" and get_occupied_direction_seats_number(i, j) >= 5:
                buffer_area_map[i][j] = "L"
                change = True
    area_map = deepcopy(buffer_area_map)

occupied_seats = 0
for i in range(ROWS):
    for j in range(COLUMNS):
        if area_map[i][j] == "#":
            occupied_seats += 1
print(occupied_seats)
