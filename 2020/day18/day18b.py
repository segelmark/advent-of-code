import re  
from validationdata import *

def parentheses(data):
    return (re.sub("\((\d+)\)",r"\1",
                data))

def add(data):
    return (re.sub("(\d+) \+ (\d+)",
                lambda m: str(int(m.group(1))+int(m.group(2))),
                data))

def multiplyPare(data):
    return (re.sub("\((\d+) \* (\d+)\)",
                lambda m: str(int(m.group(1))*int(m.group(2))),
                data))

def multiplyPareEnd(data):
    return (re.sub("\* (\d+) \* (\d+)\)",
                lambda m: "* "+str(int(m.group(1))*int(m.group(2)))+")",
                data))

def multiply(data):
    return (re.sub("(\d+) \* (\d+)",
                lambda m: str(int(m.group(1))*int(m.group(2))),
                data))

for v in validationdata:
    pass

def evaluate(d):
    d0=""
    while "(" in d and d0!=d:
        d0=d
        d1=""
        while d1!=d:
            d1=d
            d=add(d)
            d=parentheses(d)
            d=multiplyPare(d)
        d=multiplyPareEnd(d)
    d0=""
    while "+" in d and d0!=d:
        d=add(d)
    
    while "*" in d:
        d=multiply(d)
    # print(d)
    return int(d)

assert sum(evaluate(expression) for expression in validationdata) == 231+51+46+1445+669060+23340

with open("input.txt") as f:
    data = [x.strip() for x in f]
print(sum(evaluate(expression) for expression in data))