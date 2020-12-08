input_file = open("input", "r")
instructions = [(instruction.split()[0], int(instruction.split()[1])) for instruction in input_file.readlines()]
input_file.close()

value = 0
current_index = 0
visited_index = []

while current_index not in visited_index:
    visited_index.append(current_index)
    if instructions[current_index][0] == "acc":
        value += instructions[current_index][1]
        current_index += 1
    elif instructions[current_index][0] == "jmp":
        current_index += instructions[current_index][1]
    elif instructions[current_index][0] == "nop":
        current_index += 1

print(value)
