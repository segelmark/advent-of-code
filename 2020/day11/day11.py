from validationdata import *

def convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1

def renderMap(seat_map):
    for line in seat_map:
        s = "" 
        print(s.join(line))

def count_occupied_adj(pos,seats):
    y=pos[0]
    x=pos[1]
    maxY=len(seats)-1
    maxX=len(seats[0])-1
    occupied="#"
    c=0
    if y>0:
        if x>0 and seats[y-1][x-1]==occupied: c+=1
        if seats[y-1][x]==occupied: c+=1
        if x<maxX and seats[y-1][x+1]==occupied: c+=1
    if y<maxY:
        if x>0 and seats[y+1][x-1]==occupied: c+=1
        if seats[y+1][x]==occupied: c+=1
        if x<maxX and seats[y+1][x+1]==occupied: c+=1
    if x>0 and seats[y][x-1]==occupied: c+=1
    if x<maxX and seats[y][x+1]==occupied: c+=1
    return c

def count_occupied_visible(pos,seats):
    y0=pos[0]
    x0=pos[1]
    maxY=len(seats)
    maxX=len(seats[0])
    occupied="#"
    free="L"
    c=0
    directions=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    for d in directions:
        y=y0+0
        x=x0+0
        while((y>=0 and y<maxY and x>=0 and x<maxX)):
            y+=d[0]
            x+=d[1]
            if not (y>=0 and y<maxY and x>=0 and x<maxX):
                break
            check=seats[y][x]
            if check==occupied:
                c+=1
                break
            if check==free:
                break
    return c

print(count_occupied_visible([4,3],v8))

def applyRule(seat_map):
    new_map=[]
    for y, line in enumerate(seat_map):
        new_map.append(seat_map[y].copy())
        for x, char in enumerate(line):
            if char == "L" and count_occupied_visible([y,x],seat_map)==0: # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
                new_map[y][x]="#"
            if char == "#" and count_occupied_visible([y,x],seat_map)>=5: # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
                new_map[y][x]="L"
    return new_map

def countCharacters(char, seat_map):
    c=0
    for row in seat_map:
        c+=row.count(char)
    return c

def day11(data):
    seat_map=[convert(line) for line in data]
    newcount=countCharacters("#",seat_map)
    oldcount=1
    while(oldcount!=newcount):
        # renderMap(seat_map)
        seat_map=applyRule(seat_map)
        oldcount=newcount
        newcount=countCharacters("#",seat_map)
    return countCharacters("#",seat_map)

# assert day11(validationdata)==37

print(day11(validationdata))

f = open("input.txt", "r")
data = f.read().splitlines()

print(day11(data))