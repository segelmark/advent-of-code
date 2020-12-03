import itertools
import numpy 

validation = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".splitlines()

f = open("input.txt", "r")
data = f.read().splitlines()

"""
    Recursive implementation
"""
def navigate(geomap,rule,count=0,x=0):
    x=x+rule[0]
    if x>=len(geomap[0]):
        x -= len(geomap[0])
    if(geomap[rule[1]][x]=="#"):
        count=count+1
    if(len(geomap[rule[1]:])<=rule[1]):
        return count
    return navigate(geomap[rule[1]:],rule,count,x)

def run_rules(geomap, rules):
    result=[]
    for rule in rules: result.append(navigate(geomap,rule))
    return result

rules=[[1,1],[3,1],[5,1],[7,1],[1,2]]

assert run_rules(validation, rules)==[2, 7, 3, 4, 2]

result=run_rules(data, rules)
print(result)
print(numpy.prod(result))

"""
    First implementation
"""
def repeat_to_length(string_to_expand, length):
    return list((string_to_expand * (int(length/len(string_to_expand))+1))[:length])

def render_map(geomap):
    for line in geomap:
        print("".join(line))

def traverse(travelmap,step_x,step_y):
    x=step_x
    y=step_y
    trees=0
    while(y<len(travelmap)):
        if(travelmap[y][x]=="."):
            travelmap[y][x]="O"
        else:
            travelmap[y][x]="X"
            trees+=1
        x=x+step_x
        y=y+step_y
    return [travelmap, trees]

def day3(data,render=False):
    geomap = list(map(repeat_to_length,data,itertools.repeat(len(data)*7,len(data))))
    rules=[[1,1],[3,1],[5,1],[7,1],[1,2]]
    result=[]
    for rule in rules:
        [treemap, trees] = traverse(geomap,rule[0],rule[1])
        result.append(trees)
        if(render):
            render_map(treemap)
            print(trees)
    return result

assert(day3(validation)==[2, 7, 3, 4, 2])

result=day3(data)
print(result)
print(numpy.prod(result))

