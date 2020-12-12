from copy import deepcopy
input_file = open("input", "r")
area_map = [[symbol for symbol in row.replace("\n", "")] for row in input_file.readlines()]
input_file.close()

ROWS = len(area_map)
COLUMNS = len(area_map[0])

buffer_area_map = [['.' for j in range(COLUMNS+2)] for i in range(ROWS+2)]
for i in range(1, ROWS+1):
    for j in range(1, COLUMNS+1):
        buffer_area_map[i][j] = area_map[i-1][j-1]

area_map = deepcopy(buffer_area_map)

def get_occupied_adjacent_seats_number(row, column):
    field_value = lambda i, j:  1 if area_map[i][j] == "#" else 0
    number = field_value(row-1, column-1)
    number += field_value(row-1, column)
    number += field_value(row-1, column+1)
    number += field_value(row, column+1)
    number += field_value(row, column-1)
    number += field_value(row+1, column-1)
    number += field_value(row+1, column)
    number += field_value(row+1, column+1)
    return number


change = True
while change:
    change = False
    for i in range(1, ROWS+1):
        for j in range(1, COLUMNS+1):
            if area_map[i][j] == "L" and get_occupied_adjacent_seats_number(i, j) == 0:
                buffer_area_map[i][j] = "#"
                change = True
            elif area_map[i][j] == "#" and get_occupied_adjacent_seats_number(i, j) >= 4:
                buffer_area_map[i][j] = "L"
                change = True
    area_map = deepcopy(buffer_area_map)

occupied_seats = 0
for i in range(1, ROWS + 1):
    for j in range(1, COLUMNS + 1):
        if area_map[i][j] == "#":
            occupied_seats += 1
print(occupied_seats)
