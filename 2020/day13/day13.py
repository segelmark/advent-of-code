from validationdata import *
from math import gcd
from functools import reduce

def waitTimes(data):
    last_arrival={}
    wait_times={}
    for bus in data[1:]:
        if not bus=="x":
            last_arrival[bus]=data[0]//bus*bus
            wait_times[bus]=last_arrival[bus]+bus-data[0]
            # print(f"Bus {bus} last arrived {last_arrival[bus]} next bus at {last_arrival[bus]+bus}")
    return wait_times

def next_bus(data):
    wait_time=waitTimes(data)
    best_bus=min(wait_time, key=wait_time.get)
    return best_bus, wait_time[best_bus]

def part1(data):
    data=data.replace("\n",",").split(",")
    data=[int(l) if l!="x" else "x" for l in data]
    bus_number, wait_time=next_bus(data)
    return bus_number*wait_time

def findMatch(buses,constants,i=0,step=1):
    print(buses)
    print(constants)
    if i==0:
        i+=step
    while(True):
        valid=True
        for j, bus in enumerate(buses):
            if not(i+constants[j])%buses[j]==0:
                valid=False
        if valid:
            print(i)

            return i
        i+=step

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

def part2(data):
    data=[int(l) if l!="x" else "x" for l in data.split(",")]
    print(reduce((lambda x, y: x * y), [l for l in data if l!="x"]))
    buses=[]
    constants=[]
    for i, bus in enumerate(data):
        if not bus=="x":
           buses.append(bus)
           constants.append(i)
    step=buses[0]
    i=0
    j=2
    while(j<len(buses)):
        i=findMatch(buses[0:j+1],constants[0:j+1],i,step)
        step=lcm(buses[0:j+1])
        j+=1
    return i   

assert part2("17,x,13,19") == 3417
assert part2("67,7,59,61") == 754018
assert part2("67,x,7,59,61") == 779210
assert part2("67,7,x,59,61") == 1261476
assert part2("1789,37,47,1889") == 1202161486

assert part1(validationdata) == 295

f = open("input.txt", "r")
data = f.read()

print(part1(data))
part2(str(data.splitlines()[1]))
