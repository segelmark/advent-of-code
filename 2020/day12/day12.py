from validationdata import *

def navigate(param,value,pos):
    """ Action N/S/E/W means to move ship or waypoint north/south/east/west by the given value. """
    direction={"N":[1,0],"E":[0,1],"S":[-1,0],"W":[0,-1]}
    return [pos[0]+direction[param][0]*value,pos[1]+direction[param][1]*value]

def rotateWaypoint(param,value,pos,wp):
    """ Action R now means to rotate the waypoint around the ship right (clockwise) the given number of degrees. """
    waypoint={90:[-wp[1],wp[0]],180:[-wp[0],-wp[1]],270:[wp[1],-wp[0]]}
    if param=="L" and (value==90 or value==270): value=(value+180)%360 # turning left is like turning right backwards
    return pos, waypoint[value]

def moveToWaypoint(param,value,pos,waypoint):
    """ Action F now means to move to the waypoint a number of times equal to the given value. """
    return [pos[0]+waypoint[0]*value,pos[1]+waypoint[1]*value], waypoint

def executeCommand(param,value,pos,waypoint,mode="default"):
    if(mode=="waypoint" and param in ["N","W","E","S"]): return pos, navigate(param,value,waypoint)
    elif(mode=="default" and param in ["N","W","E","S"]): return navigate(param,value,pos), waypoint
    elif(param in ["L","R"]): return rotateWaypoint(param,value,pos,waypoint)
    elif(param == "F"): return moveToWaypoint(param,value,pos,waypoint)

def runShip(instructions,mode="default",waypoint=[0,1]):
    pos=[0,0]
    if(mode=="waypoint"): waypoint=[1,10]
    for inst in instructions:
        pos, waypoint = executeCommand(inst[0],int(inst[1:]),pos,waypoint,mode)
    return pos

assert runShip(validationdata)==[-8,17]
assert runShip(validationdata,"waypoint") == [-72, 214]

def manhattan(data):
    return abs(data[0])+abs(data[1])

assert manhattan(runShip(validationdata)) == 25
assert manhattan(runShip(validationdata,"waypoint")) == 286

f = open("input.txt", "r")
data = f.read().splitlines()

print(manhattan(runShip(data))) # Part 1
print(manhattan(runShip(data,"waypoint"))) # Part 2