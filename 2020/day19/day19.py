from validationdata import *

def parseInput(data):
    input=data.split("\n\n")
    rules={}
    for rule in input[0].splitlines():
        r=rule.split(": ")
        rules[r[0]]=[l.replace('"','').split(" ") for l in r[1].split(" | ")]
    examples=input[1].splitlines()
    return rules, examples

# def runRule(rules, string, ruleNum=0, pos=0, depth=0):
#     valid=False
#     print(f"Rule: {ruleNum} Position: {pos} Depth: {depth}")
#     for i, r in enumerate(rules[ruleNum]):
#         if r[0]=="a" or r[0]=="b":
#             print(r[0])
#             print(string[pos])
#             if(string[pos]==r[0]): return True
#             else: return False
#         else:
#             v1, d1 = runRule(rules, string, int(r[0]), pos, depth+1)
#             v2, d2 = runRule(rules, string, int(r[1]), pos, depth+1)
#             if v1 or v2:
#                 valid=True
#     return valid, depth
#         # r=rule.split(" ")
#         # runRule(rules, int(r), string)


def getValidStrings(rules,r0="0"):
    branches=rules[r0].copy()
    for j, branch in enumerate(branches):
        i=0
        while i<len(branch):
            if branch[i]!="a" and branch[i]!="b":
                if len(rules[branch[i]])>1:
                    new_branch=branch.copy()
                    for char2 in rules[branch[i]][1]:
                        new_branch.insert(i+1, char2)
                    new_branch.pop(i)
                    branches.insert(j+1, new_branch)
                for char1 in rules[branch[i]][0]:
                    branch.insert(i+1, char1)
                branch.pop(i)
            while not branch[i].isnumeric():
                i+=1
                if i==len(branch):
                    break 
    return branches



def part1(data):
    rules, examples = parseInput(data)
    print(examples)
    print(len(examples))
    branches1=getValidStrings(rules,"8")
    branches2=getValidStrings(rules,"11")
    count=0
    examples1=[]
    for branch in branches1:
        branch=''.join(map(str, branch))
        for example in examples:
            if(branch in example[:8]):
                examples1.append(example)
                count+=1
    print(count)
    count=0
    examples2=[]
    for branch in branches2:
        branch=''.join(map(str, branch))
        for example in examples:
            if(branch in example[8:24]):
                examples2.append(example)
                count+=1
    print(count)
    return len([w for w in examples1 if w in examples2 and len(w)==24])
        
# assert part1(validation0)==2
# assert part1(validation1)==8
# assert part1(validation2)==2

f = open("input.txt", "r")
data = f.read()

print(part1(data))