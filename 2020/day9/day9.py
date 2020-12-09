from validationdata import *

def makeInt(data):
    return [int(s) for s in data]

validation=makeInt(validationdata)

def checkNumber(number,sequence):
    for comp1 in sequence:
        comp2=number-comp1
        if comp2 in sequence:
            return True
    return False

assert checkNumber(576,validation) == True

def findInvalid(data,length):
    sequence=makeInt(data)
    i=length
    while(i<len(sequence)):
        if not checkNumber(sequence[i],sequence[i-length:i]):
            return sequence[i]
        i+=1

assert findInvalid(validation,5) == 127

def findRange(data,invalid):
    for i, l in enumerate(data):
        summ=0
        j=0
        while(summ<invalid):
            summ+=data[i+j]
            j+=1
        if(summ==invalid):
            return data[i:i+j]

assert findRange(validation,127) == [15, 25, 47, 40]

def encryptionWeakness(data,invalid):
    range=findRange(data,invalid)
    return max(range)+min(range)

assert encryptionWeakness(validation,127) == 62

f = open("input.txt", "r")
data = f.read().splitlines()
input = makeInt(data)

invalid=findInvalid(input,25)
print(invalid)
print(encryptionWeakness(input,invalid))

