test="R8,U5,L5,D3"
testB="U7,R6,D4,L4"
test1a="R75,D30,R83,U83,L12,D49,R71,U7,L72"
test1b="U62,R66,U55,R34,D71,R55,D58,R83"
test2a="R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
test2b="U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

intersections=[]

def render_map(map):
    for row in map:
        string=""
        for col in row:
            string+=col+" "
        print(string)

def create_blank_map(map, n):
    i=n
    while(i>0):
        map.append(["."] * n)
        i-=1
    map[x+int(n/2)][y+int(n/2)]="0"

def draw(sign, count, x, y):
    if(map[y+int(n/2)][x+int(n/2)]=="."):
        if(count==1):
            map[y+int(n/2)][x+int(n/2)]="+"
        else:
            map[y+int(n/2)][x+int(n/2)]=sign
    else:
        map[y+int(n/2)][x+int(n/2)]="X"


def run(instructions, x, y, path, map=0):
    for instruction in instructions:
        direction=instruction[0:1]
        count=int(instruction[1:])
        while(count>0):
            if(direction=="R"):
                x=x+1
                path.append((x,y))
                if(map!=0):
                    draw("-", count, x, y)
            if(direction=="L"):
                x=x-1
                path.append((x,y))
                if(map!=0):
                    draw("-", count, x, y)
            if(direction=="U"):
                y=y-1
                path.append((x,y))
                if(map!=0):
                    draw("|", count, x, y)
            if(direction=="D"):
                y=y+1
                path.append((x,y))
                if(map!=0):
                    draw("|", count, x, y)
            count=count-1

def compare_paths(pathA, pathB):
    pathA_dict = dict((k,i) for i,k in enumerate(pathA))
    pathB_dict = dict((k,i) for i,k in enumerate(pathB))
    inter = set(pathA).intersection(pathB)
    print(inter)

    list=[]
    for i in inter:
        list.append(abs(i[0]) + abs(i[1]))
    print("Distance to closest intersection: "+str(min(list)))
    steps = [ pathA_dict[x]+pathB_dict[x] for x in inter ]
    print("Minimum number of steps: "+str(min(steps)+2))

n=20
x=0
y=0
map=[]
create_blank_map(map,n)

intersections=[]
pathA=[]
run(test.split(","), x, y, pathA, map)
pathB=[]
run(testB.split(","), x, y, pathB, map)
render_map(map)

x=0
y=0

pathA=[]
run(test1a.split(","), x, y, pathA)
pathB=[]
run(test1b.split(","), x, y, pathB)

#print(intersections)
""" print("Path A:"+str(pathA))
print("Path B:"+str(pathB)) """

compare_paths(pathA, pathB)

x=0
y=0

pathA=[]
run(test2a.split(","), x, y, pathA)
pathB=[]
run(test2b.split(","), x, y, pathB)

compare_paths(pathA, pathB)


x=0
y=0

filename = "Day3/input.txt"
file = open(filename, "r")
pathA=[]
run(file.readline()[:-1].split(","), x, y, pathA)
pathB=[]
run(file.readline()[:-1].split(","), x, y, pathB)

compare_paths(pathA, pathB)