import re

input_file = open("input", "r")
re_instruction = re.compile(r"(?P<ACTION>\w)(?P<VALUE>\d*)")
instructions = [[re.match(re_instruction, instruction).group("ACTION"),
                 int(re.match(re_instruction, instruction).group("VALUE"))] for instruction in input_file.readlines()]
input_file.close()

position = [0, 0]
direction = [1, 0]

for instruction in instructions:
    if instruction[0] == "W":
        position[0] -= instruction[1]
    elif instruction[0] == "E":
        position[0] += instruction[1]
    elif instruction[0] == "N":
        position[1] -= instruction[1]
    elif instruction[0] == "S":
        position[1] += instruction[1]
    elif instruction[0] == "F":
        position[0] += direction[0] * instruction[1]
        position[1] += direction[1] * instruction[1]
    elif instruction[0] == "R":
        for turns in range(int(instruction[1] / 90)):
            if direction == [1, 0]:
                direction = [0, 1]
            elif direction == [0, 1]:
                direction = [-1, 0]
            elif direction == [-1, 0]:
                direction = [0, -1]
            elif direction == [0, -1]:
                direction = [1, 0]
    elif instruction[0] == "L":
        for turns in range(int(instruction[1] / 90)):
            if direction == [1, 0]:
                direction = [0, -1]
            elif direction == [0, 1]:
                direction = [1, 0]
            elif direction == [-1, 0]:
                direction = [0, 1]
            elif direction == [0, -1]:
                direction = [-1, 0]

print(position)
print(abs(position[0]) + abs(position[1]))
