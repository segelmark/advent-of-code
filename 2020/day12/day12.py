from validationdata import *

def navigate(param,value,pos):
    """
        Action N/S/E/W means to move north/south/east/west by the given value.
    """
    if(param=="N"): new_pos=[pos[0]+value,pos[1]]
    elif(param=="E"): new_pos=[pos[0],pos[1]+value]
    elif(param=="S"): new_pos=[pos[0]-value,pos[1]]
    elif(param=="W"): new_pos=[pos[0],pos[1]-value]
    else: print(f"Weird! Cannot navigate {param}")
    return new_pos

def moveForward(param,value,pos,direction):
    """
        Action F means to move forward by the given value in the direction the ship is currently facing.
    """
    if(direction==0): bearing="N"
    elif(direction==90): bearing="E"
    elif(direction==180): bearing="S"
    elif(direction==270): bearing="W"
    else: print(f"Not straight enough {direction}")
    return navigate(bearing,value,pos), direction

def turn(param,value,pos,direction):
    """
        # Action R/L means to turn right/left the given number of degrees.
    """
    if(param=="R"): return pos, (direction+value)%360 
    elif(param=="L"): return pos, (direction-value)%360
    else: print(f"Cannot turn: {param}")

def executeCommand(param,value,pos,direction):
    if(param in ["N","W","E","S"]): return navigate(param,value,pos), direction
    elif(param in ["L","R"]): return turn(param,value,pos,direction)
    elif(param == "F"): return moveForward(param,value,pos,direction)

def runA(instructions):
    pos=[0,0]
    direction=90
    for inst in instructions:
        pos, direction = executeCommand(inst[0],int(inst[1:]),pos,direction)
    return pos

assert runA(validationdata) == [-8, 17]

def turnWaypoint(param,value,pos,wp):
    if param=="L":
        if(value==90): value=270
        elif(value==270): value=90
    if(value==90): wp=[-wp[1],wp[0]]
    elif(value==180): wp=[-wp[0],-wp[1]]
    elif(value==270): wp=[wp[1],-wp[0]]
    else: print(f"Cannot turn waypoint: {value}")
    return pos, wp

def moveToWaypoint(param,value,pos,waypoint):
    return [pos[0]+waypoint[0]*value,pos[1]+waypoint[1]*value], waypoint

def executeWaypoint(param,value,pos,waypoint):
    if(param in ["N","W","E","S"]): return pos, navigate(param,value,waypoint)
    elif(param in ["L","R"]): return turnWaypoint(param,value,pos,waypoint)
    elif(param == "F"): return moveToWaypoint(param,value,pos,waypoint)

def runB(instructions):
    waypoint=[1,10] #relative to ship
    pos=[0,0]
    for inst in instructions:
        pos, waypoint = executeWaypoint(inst[0],int(inst[1:]),pos,waypoint)
    return pos

assert runB(validationdata) == [-72, 214]

def manhattan(instructions,func=runA):
    pos = func(instructions)
    return abs(pos[0])+abs(pos[1])

assert manhattan(validationdata,runA) == 25
assert manhattan(validationdata,runB) == 286

f = open("input.txt", "r")
data = f.read().splitlines()

print(manhattan(data,runA))
print(manhattan(data,runB))