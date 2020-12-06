input_file = open("input", "r")
seats = input_file.read().split()
input_file.close()


def calculate_seat_id(seat):
    row = _binary_chose(seat[:7], 0, 127)
    column = _binary_chose(seat[7:], 0, 7)
    return row * 8 + column


def _binary_chose(seat, start, end):
    if start == end:
        return start
    else:
        middle = (end-start)//2 + start
        if seat[0] in ("F", "L"):
            return _binary_chose(seat[1:], start, middle)
        else:
            return _binary_chose(seat[1:], middle+1, end)

seats_ids = []
highest_seat = -1
for seat in seats:
    seat_id = calculate_seat_id(seat)
    seats_ids.append(seat_id)
    if seat_id > highest_seat:
        highest_seat = seat_id

print(highest_seat)

#part2
seats_ids.sort()
for i in range(len(seats_ids)-1):
    if seats_ids[i+1] - seats_ids[i] != 1:
        print(seats_ids[i]+1)
