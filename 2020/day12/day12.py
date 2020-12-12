from validationdata import *

def navigate(param,value,pos):
    """ Action N/S/E/W means to move ship or waypoint north/south/east/west by the given value. """
    new_pos={"N":[1,0],"E":[0,1],"S":[-1,0],"W":[0,-1]}
    return [pos[0]+new_pos[param][0]*value,pos[1]+new_pos[param][1]*value]

def moveForward(param,value,pos,direction):
    """ Action F means to move forward by the given value in the direction the ship is currently facing. """
    bearing={"0":"N","90":"E","180":"S","270":"W"}
    return navigate(bearing.get(str(direction)),value,pos), direction

def turn(param,value,pos,direction):
    """ Action R/L means to turn right/left the given number of degrees. """
    return pos, (direction+value*(1 if param=="R" else -1))%360 

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
    """ Action R now means to rotate the waypoint around the ship right (clockwise) the given number of degrees. """
    if param=="L": # turning left is like turning right backwards
        if(value==90): value=270
        elif(value==270): value=90
    if(value==90): wp=[-wp[1],wp[0]]
    elif(value==180): wp=[-wp[0],-wp[1]]
    elif(value==270): wp=[wp[1],-wp[0]]
    return pos, wp

def moveToWaypoint(param,value,pos,waypoint):
    """ Action F now means to move to the waypoint a number of times equal to the given value. """
    return [pos[0]+waypoint[0]*value,pos[1]+waypoint[1]*value], waypoint

def executeWaypoint(param,value,pos,waypoint):
    if(param in ["N","W","E","S"]): return pos, navigate(param,value,waypoint)
    elif(param in ["L","R"]): return turnWaypoint(param,value,pos,waypoint)
    elif(param == "F"): return moveToWaypoint(param,value,pos,waypoint)

def runB(instructions):
    waypoint=[1,10] # waypoint position relative to ship
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