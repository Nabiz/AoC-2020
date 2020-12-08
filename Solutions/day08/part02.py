input_file = open("input", "r")
base_instructions = [[instruction.split()[0], int(instruction.split()[1])] for instruction in input_file.readlines()]
input_file.close()


def execute_instructions(instructions):
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
        if current_index >= len(instructions):
            return value
    return None


def main():
    current_instruction_index = 0
    while current_instruction_index < len(base_instructions):
        if base_instructions[current_instruction_index][0] == "nop":
            base_instructions[current_instruction_index][0] = "jmp"
            result = execute_instructions(base_instructions)
            if result:
                return result
            else:
                base_instructions[current_instruction_index][0] = "nop"
        elif base_instructions[current_instruction_index][0] == "jmp":
            base_instructions[current_instruction_index][0] = "nop"
            result = execute_instructions(base_instructions)
            if result:
                return result
            else:
                base_instructions[current_instruction_index][0] = "jmp"
        current_instruction_index += 1


if __name__ == '__main__':
    print(main())
