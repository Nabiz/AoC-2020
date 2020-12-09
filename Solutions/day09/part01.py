input_file = open("input", "r")
number_series = [int(line) for line in input_file.readlines()]
input_file.close()

p = 0
q = 25


def check_number(preamble, checked_number):
    for i in range(len(preamble)-1):
        for j in range(i+1, len(preamble)):
            if preamble[i]+preamble[j] == checked_number:
                return True
    return False


invalid_number = None
for number in number_series[25:]:
    if not check_number(number_series[p:q], number):
        invalid_number = number
        break
    p += 1
    q += 1
print(invalid_number)


#PART2
p = 0
q = 1
invalid_set_sum = number_series[p]
while True:
    if invalid_number > invalid_set_sum:
        invalid_set_sum += number_series[q]
        q += 1
    elif invalid_number < invalid_set_sum:
        invalid_set_sum -= number_series[p]
        p += 1
    elif invalid_number == invalid_set_sum:
        invalid_set = number_series[p:q]
        break

print(min(invalid_set) + max(invalid_set))