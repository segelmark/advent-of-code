from validationdata import *

def evaluate(instruction, pos, acc):
    inst=instruction.split(" ")
    if inst[0]=="jmp":
        if(inst[1]=="+0"):
            pos+=1
        else:
            pos+=int(inst[1])
    elif inst[0]=="acc":
        acc+=int(inst[1])
        pos+=1
    elif inst[0]=="nop":
        pos+=1
    return pos, acc

def run_code(code):
    pos=0
    acc=0
    history=[]
    while(True):
        if(pos in history[:-1]):
            return acc, False
        pos, acc = evaluate(code[pos], pos, acc)
        history.append(pos)
        if(pos==len(code)-1):
            return acc, True
    return acc, True

assert run_code(validation)==(5, False)
assert run_code(validation2)==(2, True)

def debug(code):
    for pos, l in enumerate(code):
        improved_code=code.copy()
        if(code[pos][:3]=="nop"):
            improved_code[pos]="jmp"+code[pos][3:]
        elif(code[pos][:3]=="jmp"):
            improved_code[pos]="nop"+code[pos][3:]
        acc, test=run_code(improved_code)
        if(test):
            return acc
        pos+=1

f = open("input.txt", "r")
data = f.read().splitlines()

print(run_code(data))
print(debug(data))