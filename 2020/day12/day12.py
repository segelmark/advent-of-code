from validationdata import *

def navigate(action,value,pos):
    """ Action N/S/E/W means to move ship or waypoint north/south/east/west by the given value. """
    direction={ "N": [1,0],
                "E": [0,1],
                "S": [-1,0],
                "W": [0,-1]}
    return [pos[0]+direction[action][0]*value,
            pos[1]+direction[action][1]*value]

def rotateWaypoint(action,value,pos,wp):
    """ Action R rotates the waypoint around the ship right (clockwise) the given number of degrees. """
    waypoint={  90:[ -wp[1], wp[0] ],
                180:[ -wp[0], -wp[1] ],
                270:[ wp[1], -wp[0] ] }
    if action=="L" and (value==90 or value==270): # turning left is like turning right backwards
        value=(value+180)%360 
    return waypoint[value]

def moveToWaypoint(action,value,pos,waypoint):
    """ Action F moves to the waypoint a number of times equal to the given value. """
    return [pos[0]+waypoint[0]*value,
            pos[1]+waypoint[1]*value]

def executeCommand(action,value,pos,waypoint,mode="default"):
    """ The right function depends on the action as well as the mode of vessel navigation """
    if mode=="default" and action in ["N","W","E","S"]:
        return navigate(action,value,pos), waypoint
    elif mode=="waypoint" and action in ["N","W","E","S"]:
        return pos, navigate(action,value,waypoint)
    elif action in ["L","R"]:
        return pos, rotateWaypoint(action,value,pos,waypoint)
    elif action == "F":
        return moveToWaypoint(action,value,pos,waypoint), waypoint

def sailShip(instructions,mode="default",waypoint=[0,1]):
    """ Automatically sails ships on discrete grids according to instructions """
    pos=[0,0]
    for inst in instructions:
        pos, waypoint = executeCommand(inst[0], int(inst[1:]), pos, waypoint, mode)
    return pos

def manhattan(data):
    return abs(data[0])+abs(data[1])

assert manhattan(sailShip(validationdata)) == 25
assert manhattan(sailShip(validationdata,"waypoint",[1,10])) == 286

f = open("input.txt", "r")
data = f.read().splitlines()

print(manhattan(sailShip(data))) # Part 1
print(manhattan(sailShip(data,"waypoint",[1,10]))) # Part 2