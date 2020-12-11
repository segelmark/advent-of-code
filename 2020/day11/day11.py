from validationdata import *

def convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1

def renderMap(seat_map):
    for line in seat_map:
        s = "" 
        print(s.join(line))

def count_occupied_visible(pos,seats,visibility=0):
    if not visibility:
        visibility=len(seats)
    c=0
    directions=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    for d in directions:
        y=pos[0]+0
        x=pos[1]+0
        i=0
        while(i<visibility):
            y+=d[0]
            x+=d[1]
            if not (y>=0 and y<len(seats) and x>=0 and x<len(seats[0])):
                break
            check=seats[y][x]
            if check=="#": #occupied
                c+=1
                break
            if check=="L": #free
                break
            i+=1
    return c

assert count_occupied_visible([4,3],v8) == 8
assert count_occupied_visible([4,3],v8,1) == 2

def applyRule(seat_map,visibility=0):
    new_map=[]
    for y, line in enumerate(seat_map):
        new_map.append(seat_map[y].copy())
        for x, char in enumerate(line):
            if char == "L" and count_occupied_visible([y,x],seat_map,visibility)==0: # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
                new_map[y][x]="#"
            if char == "#" and count_occupied_visible([y,x],seat_map,visibility)>=5-visibility: # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
                new_map[y][x]="L"
    return new_map

def countCharacters(char, seat_map):
    c=0
    for row in seat_map:
        c+=row.count(char)
    return c

def day11(data,visibility=0):
    seat_map=[convert(line) for line in data]
    newcount=countCharacters("#",seat_map)
    oldcount=1
    while(oldcount!=newcount):
        # renderMap(seat_map)
        seat_map=applyRule(seat_map,visibility)
        oldcount=newcount
        newcount=countCharacters("#",seat_map)
    return countCharacters("#",seat_map)

assert day11(validationdata,1)==37 # Run with visibility limited to 1
assert day11(validationdata)==26 # See further!

f = open("input.txt", "r")
data = f.read().splitlines()

print(day11(data,1)) # Run with visibility limited to 1
print(day11(data)) # See further!