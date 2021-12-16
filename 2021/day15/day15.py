import time
import heapq

validation = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

correctAnswer1 = 40
correctAnswer2 = 315

def day15(data,part=1):
    data = [[int(x) for x in y] for y in data.splitlines()]
    dim=len(data)

    # For part 2 let's make it big - five times larger in both dimensions with every step i either direction adding 1
    if part==2:
        big_data=list()
        for a in range(0,5):
            for i in range(0,dim):
                big_data.append([])
                for b in range(0,5):
                    for j in range(0,dim):
                        new=(data[i][j]+a+b)%9
                        if(new==0): new=9
                        big_data[a*dim+i].append(new)
        data=big_data
        dim=len(data)

    # Assume every point has high cost until proven otherwise
    shortest_distance=[ [ 1e9 for x in range(0,dim) ] for y in range(0,dim) ]
    
    # Except for the start
    shortest_distance[0][0]=0 
    distances = [ (0, (0,0)) ] 

    heapq.heapify(distances) # Let's use a heap as a minimum prioritized queue so that it doesn't take an 2 hours

    unvisited=set() # Sets have a time complexity of O(1) when removing - lists not... save another hour
    for i in range(0,dim):
        for j in range(0,dim):
            unvisited.add((i,j))

    while distances:
        cost, c = heapq.heappop(distances) # Get lowest cost and next current position as c from the heap
        neighbors = [ (c[0]+1, c[1]), (c[0]-1, c[1]), (c[0], c[1]+1), (c[0], c[1]-1) ]
        for n in neighbors:
            if n in unvisited:
                new=cost+data[n[0]][n[1]]
                if(new<shortest_distance[n[0]][n[1]]):
                    shortest_distance[n[0]][n[1]]=new
                    heapq.heappush(distances, (new, n))
        unvisited.remove(c)

    return shortest_distance[dim-1][dim-1]

# Make sure everything looks OK
assert day15(validation,1) == correctAnswer1
assert day15(validation,2) == correctAnswer2

f = open("input.txt", "r")
data = f.read()

start = time.time()
print(day15(data))
end = time.time()

print("Runtime of the part 1 is " + str(end - start))

start = time.time()
print(day15(data,2))
end = time.time()

print("Runtime of the part 2 is " + str(end - start))

