import re
from math import copysign

input_file = open("input", "r")
re_instruction = re.compile(r"(?P<ACTION>\w)(?P<VALUE>\d*)")
instructions = [[re.match(re_instruction, instruction).group("ACTION"),
                 int(re.match(re_instruction, instruction).group("VALUE"))] for instruction in input_file.readlines()]
input_file.close()

position = [0, 0]
waypoint = [10, -1]

for instruction in instructions:
    if instruction[0] == "W":
        waypoint[0] -= instruction[1]
    elif instruction[0] == "E":
        waypoint[0] += instruction[1]
    elif instruction[0] == "N":
        waypoint[1] -= instruction[1]
    elif instruction[0] == "S":
        waypoint[1] += instruction[1]
    elif instruction[0] == "F":
        position[0] += waypoint[0] * instruction[1]
        position[1] += waypoint[1] * instruction[1]

    elif instruction[0] == "R":
        for turns in range(int(instruction[1] / 90)):
            new_waypoint = [0, 0]
            new_waypoint[0] = -waypoint[1]
            new_waypoint[1] = waypoint[0]
            waypoint = new_waypoint

    elif instruction[0] == "L":
        for turns in range(int(instruction[1] / 90)):
            new_waypoint = [0, 0]
            new_waypoint[0] = waypoint[1]
            new_waypoint[1] = -waypoint[0]
            waypoint = new_waypoint

print(position)
print(abs(position[0]) + abs(position[1]))
