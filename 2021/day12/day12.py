from os import initgroups
import copy


validation1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

validation2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

validation3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

correctAnswer1 = 10
correctAnswer2 = 19
correctAnswer3 = 226

def nextSteps(data,position,history=["start"]):
    if(position=="end"):
        # print(history)
        return [["end"]]
    else:
        new_data=copy.deepcopy(data)
        nextsteps=[]
        for i in range(len(data)):
            if data[i][0]==position:
                nextsteps.append(data[i][1])
                if(position.islower()):
                    new_data.pop(new_data.index(data[i]))
            elif data[i][1]==position:
                nextsteps.append(data[i][0])
                if(position.islower()):
                    new_data.pop(new_data.index(data[i]))
        return [ [position] + path for next in nextsteps for path in nextSteps(new_data,next,history+[next]) ]

        
def dayX(data):
    data = [x.split('-') for x in data.splitlines()]

    return len(nextSteps(data,"start"))

# Make sure everything looks OK
# assert dayX(validation1) == correctAnswer1
# assert dayX(validation2) == correctAnswer2
# assert dayX(validation3) == correctAnswer3

print(dayX(validation1))


f = open("input.txt", "r")
data = f.read()

# print(dayX(data))

# Make sure everything looks OK again
# assert dayXb(validation) == correctAnswer2
# print(dayXb(validation))

# print(dayXb(data))
