input_file = open("input", "r")
timestamp = int(input_file.readline())
bus_list = input_file.readline().split(",")

available_buses = [int(bus) for bus in bus_list if bus != 'x']

min_wait_time = max(available_buses)
result = None
for bus in available_buses:
    remainder = timestamp % bus
    wait_time = bus - remainder
    if wait_time < min_wait_time:
        min_wait_time = wait_time
        result = bus * min_wait_time
print(result)

# part2
bus_list = [{"offset": remainder, "number": int(number)} for remainder, number in enumerate(bus_list) if number != "x"]

t = bus_list[0]["number"]
increase = bus_list[0]["number"]
for number in bus_list[1:]:
    while (t+number["offset"]) % number["number"]:
        t += increase
    increase *= number["number"]
print(t)
