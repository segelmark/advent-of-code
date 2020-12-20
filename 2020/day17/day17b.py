from validationdata import *
import copy 
import time

start = time.time()

def initialize(initial_state):
    dim=len(initial_state)*4
    space =[ [] for i in range(-dim, dim) ] 
    for x, s in enumerate(space):
        space[x]=[ [] for i in range(-dim, dim) ]
        for y, t in enumerate(space[x]):
            space[x][y] = [ [] for i in range(-dim, dim) ]
            for z, u in enumerate(space[x][y]):
                space[x][y][z] = [ [] for i in range(-dim, dim) ]
    for i, row in enumerate(initial_state):
        for j, char in enumerate(row):
            space[i+int(dim)][j+int(dim)][int(dim)][int(dim)]  = char
    return space

def countActive(space):
    count=0
    for x in space:
        for y in x:
            for z in y:
                for w in z:
                    if w=="#":
                        count+=1
    return count

def countActiveNeighbors(space,p):
    count=0
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                for l in range(-1,2):
                    if space[p[0]+i][p[1]+j][p[2]+k][p[3]+l]=="#" and not i==j==k==l==0:
                        count+=1
    return count

def updateSpace(space,t,initial_width):
    new_space=copy.deepcopy(space)
    min=int(len(space)/2-initial_width-t-1)
    max=len(space)/2+initial_width+t+1
    x=min
    while x<max:
        y=min
        while y<max:
            z=min
            while z<max:
                w=min
                while w<max:
                    if space[x][y][z][w]=="#":
                        active=countActiveNeighbors(space, (x, y, z, w))
                        if  active!=2 and active!=3:        
                            new_space[x][y][z][w]="." 
                    else:                              
                        if countActiveNeighbors(space, (x, y, z, w))==3:
                            new_space[x][y][z][w]="#"
                    w+=1
                z+=1
            y+=1
        x+=1
    return new_space
                
def runSimulation(initial_state,cycles=6):
    space=initialize(initial_state)
    # drawPlane(space)
    t=0
    while t<cycles:
        space=updateSpace(space,t,len(initial_state))
        # drawPlane(space)
        t+=1
        print(t)
    return countActive(space)

# assert runSimulation(validationdata)==848

f = open("input.txt", "r")
data = f.read().splitlines()

print(runSimulation(data))

end = time.time()
print(end - start)