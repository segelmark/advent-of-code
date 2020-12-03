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

def repeat_to_length(string_to_expand, length):
    return list((string_to_expand * (int(length/len(string_to_expand))+1))[:length])

def render_map(geomap):
    for line in geomap:
        print("".join(line))

def traverse(geomap,step_x,step_y):
    x=step_x
    y=step_y
    trees=0
    while(y<len(geomap)):
        if(geomap[y][x]=="."):
            geomap[y][x]="O"
        else:
            geomap[y][x]="X"
            trees+=1
        x=x+step_x
        y=y+step_y
    return [geomap, trees]

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

assert(day3(validation,True)==[2, 7, 3, 4, 2])

f = open("input.txt", "r")
data = f.read().splitlines()

result=day3(data)
print(result)
print(numpy.prod(result))