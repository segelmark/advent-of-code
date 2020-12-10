from validationdata import *

def formatData(data):
    adapters=[int(s) for s in data]
    adapters.append(0)
    adapters.sort()
    return adapters

def count_differences(adapters):
    adapters=formatData(adapters)
    differences={"1" : 0, "2" :0, "3":1}
    i=1
    while i<(len(adapters)):
        differences[str(abs(adapters[i]-adapters[i-1]))]+=1
        i+=1
    return differences

assert count_differences(validationdata) == {'1': 22, '2': 0, '3': 10} 

def countPaths(adapters):
    if len(adapters)<=1:
        return 1
    paths=1
    i=2
    while i<len(adapters):
        if(adapters[i]-adapters[i-2]<=3):
            paths+=countPaths(adapters[i:])
        if(i+1<len(adapters)):      
            if(adapters[i+1]-adapters[i-2]<=3):
                paths+=countPaths(adapters[i+1:])
        i+=1
    return paths

# Do not run on full input data - it will take forever!
def day10b(data):
    return countPaths(formatData(data))

assert day10b(validation1) == 8
assert day10b(validationdata) == 19208

def splitData(data):
    last_break=0
    data_splitted=[]
    for i, l in enumerate(data):
        if(abs(data[i]-data[i-1])==3):
            data_splitted.append(data[last_break:i])
            last_break=i
    data_splitted.append(data[last_break:])
    return data_splitted

def splitAndCount(data):
    count=1
    for line in splitData(formatData(data)):
        count*=countPaths(line)
    return count

assert splitAndCount(validation1) == 8
assert splitAndCount(validationdata) == 19208

f = open("input.txt", "r")
data = f.read().splitlines()
part1=count_differences(data)
print(part1)
print(part1['1']*part1['3'])

print(splitAndCount(data))
