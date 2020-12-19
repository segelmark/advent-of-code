from validationdata import *
import re

def makeInt(value):
    return int("".join(value), 2) 

def applyMask(val,mask,char="X"):
    value=list(format(int(val),'036b'))
    for i, m in enumerate(mask):
        if m != char:
            value[i]=mask[i]
    return "".join(value)

assert applyMask(42,"000000000000000000000000000000X1001X","0")=="000000000000000000000000000000X1101X"

def getAddresses(data):
    addresses=[list(data)]
    i=0
    while(i<len(addresses)):
        for j, val in enumerate(addresses[i]):
            if val=="X":
                new_address=addresses[i].copy()
                addresses[i][j]='0'
                new_address[j]='1'
                addresses.append(new_address)
        i+=1
    return addresses
            
assert len(getAddresses("000000000000000000000000000000X1101X"))==4

def day14(data, part=1):
    instructions = [l.split(" = ") for l in data]
    memory={}
    for line in instructions:
        if line[0]=="mask": mask=line[1]
        else:
            address=re.findall(r'\d+', line[0])[0]
            if part==1:
                memory[address] = makeInt(applyMask(line[1], mask))
            elif part==2:
                for adr in getAddresses(applyMask(address,mask,"0")):
                    memory[makeInt(adr)] = int(line[1])
    return sum(memory.values())

assert day14(validationdata,1) == 165
assert day14(validation2,2) == 208

f = open("input.txt", "r")
data = f.read().splitlines()
print(day14(data))
print(day14(data,2))
