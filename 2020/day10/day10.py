from validationdata import *

def formatData(data):
    adapters=[int(s) for s in data]
    adapters.append(0)
    adapters.sort()
    return adapters

def day10(adapters):
    adapters=formatData(adapters)
    differences={"1" : 0, "2" :0, "3":1}
    i=0
    while i<(len(adapters)-1):
        differences[str(abs(adapters[i]-adapters[i+1]))]+=1
        i+=1
    return differences

assert day10(validationdata) == {'1': 22, '2': 0, '3': 10} 

def countPaths(adapters):
    if len(adapters)<=1:
        return 1
    paths=1
    i=0
    while i<(len(adapters)-2):
        if(adapters[i+2]-adapters[i]<=3):
            paths+=countPaths(adapters[i+2:])
        if(i+3<len(adapters)):      
            if(adapters[i+3]-adapters[i]<=3):
                paths+=countPaths(adapters[i+3:])
        i+=1
    return paths

# Do not run on full input data - it will take forever!
def day10b(data):
    return countPaths(formatData(data))

assert day10b(validation1) == 8
assert day10b(validationdata) == 19208

f = open("input.txt", "r")
data = f.read().splitlines()
part1=day10(data)
print(part1)
print(part1['1']*part1['3'])

print(formatData(data))


def splitData(data):
    last_break=0
    data_splitted=[]
    i=0
    while i<len(data)-1:
        if(abs(data[i+1]-data[i])==3):
            data_splitted.append(data[last_break:i+1])
            last_break=i+1
        i+=1
    data_splitted.append(data[last_break:])
    return data_splitted

def splitAndCount(data):
    count=1
    for line in splitData(formatData(data)):
        count*=countPaths(line)
    return count

assert splitAndCount(validation1) == 8
assert splitAndCount(validationdata) == 19208
print(splitAndCount(data))
