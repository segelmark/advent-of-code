validation = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".splitlines()

correctAnswer1 = 1656
correctAnswer2 = 195

def increment(data,i,j):
    if(data[i][j]!=0): data[i][j]+=1 # An octopus can only flash at most once per step.
    return data
        
def flash(data,i,j):
     # This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent.
    if(i>0):
        if(j>0): data=increment(data,i-1,j-1)
        data=increment(data,i-1,j)
        if(j<9): data=increment(data,i-1,j+1)
    if(True):
        if(j>0): data=increment(data,i,j-1)
        data=increment(data,i,j)
        if(j<9): data=increment(data,i,j+1)
    if(i<9):
        if(j>0): data=increment(data,i+1,j-1)
        data=increment(data,i+1,j)
        if(j<9): data=increment(data,i+1,j+1)
    
    data[i][j]=0 # Any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.

    return data

def counter(data,what=9):
    count=0
    for line in data:
        for num in line:
            if(num>what):
                count+=1
    return count

def day11(data,iterations=9999):
    data = [[int(y) for y in x] for x in data]

    for line in data: print(line)
    round=0
    total_count=0
    while(round<iterations):
        for i in range(10):
            for j in range(10):
                data[i][j]+=1      # First, the energy level of each octopus increases by 1.
        
        while(counter(data,9)): # This process continues as long as new octopuses keep having their energy level increased beyond 9.
            for i in range(10):
                for j in range(10):
                    if(data[i][j]>9):           # Then, any octopus with an energy level greater than 9 flashes.
                        data=flash(data,i,j)    # If this causes an octopus to have an energy level greater than 9, it also flashes.

        count=0
        for line in data: count+=line.count(0)
        
        round+=1
        if(count==100):
            return round

        total_count+=count
    return total_count

# Make sure everything looks OK
assert day11(validation,100) == correctAnswer1

f = open("input.txt", "r")
data = f.read().splitlines()

print(day11(data,100))

# Make sure everything looks OK again
assert day11(validation) == correctAnswer2

print(day11(data))
