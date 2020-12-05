
"""
The first 7 characters will either be F or B
these specify exactly one of the 128 rows on the plane (numbered 0 through 127).
Each letter tells you which half of a region the given seat is in.
Start with the whole list of rows; the first letter indicates whether the seat
is in the front (0 through 63) or the back (64 through 127).
The next letter indicates which half of that region the seat is in, and so on
until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
"""
def getRow(data):
    row = list(range(0, 128))
    for char in data[:7]:
        if char=="F":
            row = row[:int(len(row)/2)]
        else:
            row = row[int(len(row)/2):]
    return row[0]

"""
The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
"""

def getCol(data):
    col = list(range(0, 8))
    for char in data[7:]:
        if char=="L":
            col = col[:int(len(col)/2)]
        else:
            col = col[int(len(col)/2):]
    return col[0]

"""
Every seat also has a unique seat ID.
Multiply the row by 8, then add the column.
"""
def seatID(data):
    return getRow(data)*8 + getCol(data)

validation="FBFBBFFRLR"  # row 44, column 5, seat ID 357.
assert getRow(validation) == 44
assert getCol(validation) == 5
assert seatID(validation) == 357
validation="BFFFBBFRRR" #row 70, column 7, seat ID 567.
assert getRow(validation) == 70
assert getCol(validation) == 7
assert seatID(validation) == 567
validation="FFFBBBFRRR" #row 14, column 7, seat ID 119.
assert getRow(validation) == 14
assert getCol(validation) == 7
assert seatID(validation) == 119
validation="BBFFBBFRLL" #row 102, column 4, seat ID 820.
assert getRow(validation) == 102
assert getCol(validation) == 4
assert seatID(validation) == 820

f = open("input.txt", "r")
data = f.read().splitlines()

occupied = list(map(seatID,data))
maxSeat = max(occupied)
print(maxSeat)

occupied.sort()
s = len(occupied)-1
while(s>0):
    if(occupied[s]-occupied[s-1]>1):
        print(occupied[s]-1)
    s-=1


