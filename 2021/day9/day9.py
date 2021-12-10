validation = """2199943210
3987894921
9856789892
8767896789
9899965678""".splitlines()

correctAnswer1 = 15
correctAnswer2 = 1134

def getBasinSize(data,i,j,basin={}):
    x=i
    j=j
    dead_end=True
    if i>0 and (i,j) not in basin and data[i][j]<=data[i-1][j]:
        basin[(i-1,j)]=True
        dead_end=False
    else:
        basin[(i,j)]=False
    if i<len(data)-1 and number>=data[i+1][j]:
        lowest=False
    if j>0 and number>=data[i][j-1]:
        lowest=False
    if j<len(line)-1 and number>=data[i][j+1]:
        lowest=False
    


def dayX(data):
    data = [[int(y) for y in x] for x in data]
    lowpoints=[]
    basinsizes=[]
    i=0
    for line in data:
        j=0
        lowest=True
        for number in line:
            if i>0 and number>=data[i-1][j]:
                lowest=False
            if i<len(data)-1 and number>=data[i+1][j]:
                lowest=False
            if j>0 and number>=data[i][j-1]:
                lowest=False
            if j<len(line)-1 and number>=data[i][j+1]:
                lowest=False
            if(lowest):
                lowpoints.append(number)
                basinsizes.append(getBasinSize(data,i,j))
            lowest=True
            j+=1
        i+=1

    return sum([i+1 for i in lowpoints])

# Make sure everything looks OK
# assert dayX(validation) == correctAnswer1

print(dayX(validation))

f = open("input.txt", "r")
data = f.read().splitlines()

print(dayX(data))

# Make sure everything looks OK again
# assert dayXb(validation) == correctAnswer2
# print(dayXb(validation))

# print(dayXb(data))
