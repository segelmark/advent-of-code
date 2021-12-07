from validationdata import *

def flipHorizontal(edges,id):
    t=edges[id].copy()
    return [t[0],t[1],t[2][::-1],t[3][::-1]]

def flipVertical(edges,id):
    t=edges[id].copy()
    return [t[0][::-1],t[1][::-1],t[2],t[3]]

def countMatch(edges, tile, id):
    count=0
    for seq in tile:
        for key, item in edges.items():
            if seq in item and not key == id:
                count+=1
    return count
        
def parseData(data):
    return [line.replace("Tile ","").split(":\n") for line in data.split("\n\n")]

def findEdges(data):
    edges={}
    for d in data:
        edges[d[0]]=[d[1][0:10],d[1][-10:]]
        l=""
        r=""
        for i, c in enumerate(d[1]):
            if i%11==0: l+=c
            if i%11==9: r+=c
        edges[d[0]].append(l)
        edges[d[0]].append(r)
    return edges

def fixOrientation(edges):
    turns=1
    while(turns>0):
        turns=0
        for id in edges:
            if countMatch(edges, edges[id],id)<=countMatch(edges, flipHorizontal(edges,id),id):
                edges[id] = flipHorizontal(edges,id)
                print(f"Flipped horizontally around {id}")
                turns+=1
            if countMatch(edges, edges[id],id)<=countMatch(edges, flipVertical(edges,id),id):
                edges[id] = flipVertical(edges,id)
                print(f"Flipped vertically around {id}")
                turns+=1
    return edges

edges = findEdges(parseData(validationdata))

assert countMatch(edges, edges['1427'],'1427') == 4
assert countMatch(edges, edges['3079'],'3079') == 0

edges = fixOrientation(edges)

assert countMatch(edges, edges['3079'],'3079') == 2

def day20(data):
    data = parseData(data)
    edges = findEdges(data)
    edges = fixOrientation(edges)

    corners=[]
    multiply=1
    for id in edges:
        print(f"{id}: {countMatch(edges, edges[id], id)}")
        if countMatch(edges, edges[id], id)==2:
            corners.append(int(id))
            multiply=multiply*int(id)
    
    print(corners)
    return multiply

f = open("input.txt", "r")
data = f.read()

print(day20(data))
