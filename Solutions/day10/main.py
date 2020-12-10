input_file = open("input", "r")
adapters = [int(adapter) for adapter in input_file.readlines()]
input_file.close()

adapters.sort()

jolts = 0
one_jolts_diff_count = 0
three_jolts_diff_count = 1

for i in range(len(adapters)):
    if adapters[i] - jolts == 1:
        one_jolts_diff_count += 1
    elif adapters[i] - jolts == 3:
        three_jolts_diff_count += 1
    jolts = adapters[i]

print(one_jolts_diff_count * three_jolts_diff_count)

#PART2
jolts = 0
one_jolts_diff_count = 0
two_jolts_diff_count = 0
three_jolts_diff_count = 1

sequence = ""

for i in range(len(adapters)):
    sequence += str(adapters[i] - jolts)
    if adapters[i] - jolts == 1:
        one_jolts_diff_count += 1
    elif adapters[i] - jolts == 2:
        two_jolts_diff_count += 2
    elif adapters[i] - jolts == 3:
        three_jolts_diff_count += 1
    jolts = adapters[i]
sequence += '3'

print(one_jolts_diff_count, two_jolts_diff_count, three_jolts_diff_count)
print(sequence)

x = sequence.split("3")
print(x)

y = [len(_) for _ in x]
print(y)
"""
I guess answer based on knowledge:
19208 = 2^3 + 7^4
and counting '1' between '3'
[4, 4, 0, 3, 2, 0, 4, 1, 0, 4, 0]
(7 *7 *1 *4 *2 *1 *7 *1 *1 *7 *1)

I just find pattern but I need to think more about this :P
[4, 1, 2, 4, 0, 2, 0, 3, 3, 0, 0, 4, 4, 3, 0, 4, 0, 4, 2, 0, 1, 0, 4, 4, 0, 3, 2, 3, 0, 2, 4, 1, 0]
0,1 -> 1
2 -> 2
3 -> 4
4 -> 7
7*2*7*2*4*4*7*7*4*7*7*2*7*7*4*2*4*2*7 = 1322306994176
And it was right answer xD
"""
print(7*2*7*2*4*4*7*7*4*7*7*2*7*7*4*2*4*2*7)
