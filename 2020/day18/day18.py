from validationdata import *

def format(e):
    return e.replace(")"," )").replace("(","( ").split(" ")

def applyOperator(value,operator,number):
    # print(f"{value} {operator} {number}")
    if operator=="+":
        return value+int(number)
    elif operator=="*":
        return value*int(number)
    else:
        print("Warning! Weird operator!")
        assert False

def evaluate(e):
    # print(e)
    stackLevel=0
    value=[0]*100
    operator=["+"]*100
    i=0
    while i<len(e):
        if e[i].isdigit():
            value[stackLevel]=applyOperator(value[stackLevel],operator[stackLevel],e[i])
        elif e[i]=="+" or e[i]=="*":
            operator[stackLevel]=e[i]
        elif e[i]=="(":     # Move down stack
            # print(f"Level: {stackLevel} - Value: {value[stackLevel]} - Next operator: {operator[stackLevel]} ")
            stackLevel+=1
            # print(f"Level: {stackLevel} - Value: {value[stackLevel]} - Next operator: {operator[stackLevel]} ")
        elif e[i]==")":     # Move up stack
            # print(f"Level: {stackLevel} - Value: {value[stackLevel]} - Next operator: {operator[stackLevel]} ")
            operator[stackLevel]="+"
            value[stackLevel-1]=applyOperator(value[stackLevel-1],operator[stackLevel-1],value[stackLevel])
            value[stackLevel]=0
            stackLevel-=1
            # print(f"Level: {stackLevel} - Value: {value[stackLevel]} - Next operator: {operator[stackLevel]} ")
        i+=1
    return value[0]

for i, example in enumerate(validationdata):
    assert evaluate(example) == validationanswers[i]

def multiply(e):
    print(e)
    operator=None
    value=None
    i=0
    while i<len(e):
        if e[i].isdigit():
            if operator:
                new=value*int(e[i])
                operator=None
                value=None
                e[i]=""
                e[i-1]=""
                e[i-2]=str(new)
            else:
                value=int(e[i])
        elif e[i]=="*":
            operator=True
        i+=1
    return e

print(multiply(format(validationdata[0])))

def calculateResultingSums(data,part=1):
    sum=0
    for e in data:
        expression=format(e)
        if part==2: expression=multiply(expression)
        sum+=evaluate(expression)
    return sum

f = open("input.txt", "r")
data = f.read().splitlines()

print(calculateResultingSums(data))