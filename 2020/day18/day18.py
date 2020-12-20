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
            stackLevel+=1
        elif e[i]==")":     # Move up stack
            operator[stackLevel]="+"
            value[stackLevel-1]=applyOperator(value[stackLevel-1],operator[stackLevel-1],value[stackLevel])
            value[stackLevel]=0
            stackLevel-=1
        i+=1
    return value[0]

for i, example in enumerate(validationdata):
    assert evaluate(example) == validationanswers[i]

def calculateResultingSums(data,part=1):
    sum=0
    for e in data:
        expression=format(e)
        # if part==2: expression=addFirst(expression)
        sum+=evaluate(expression)
    return sum

f = open("input.txt", "r")
data = f.read().splitlines()

print(calculateResultingSums(data))

# assert calculateResultingSums(validationdata,2) == 231+51+46+1445+669060+23340