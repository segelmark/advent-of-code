from validationdata import *

def parseGroupAnswer(group):
    group_answer={}
    for pers in group:
        for ans in pers:
            if ans in group_answer:
                group_answer[ans]+=1
            else:
                group_answer[ans]=1
    return group_answer 

def getConsistentAnswers(group_answer,group_size):
    count=0
    for q in group_answer:
        if(group_answer[q]==group_size):
            count+=1
    return count

def day6a(data):
    unique_answers=[]
    consistent_answers=[]
    for group in data:
        group=group.splitlines()
        group_answer=parseGroupAnswer(group)
        unique_answers.append(len(group_answer))
        consistent_answers.append(getConsistentAnswers(group_answer,len(group)))
    return [unique_answers, consistent_answers]

test=day6a(validation)
assert test==[validResults1, validResults2]
assert sum(test[0])==11
assert sum(test[1])==6

f = open("input.txt", "r")
data = f.read().split("\n\n")

results=day6a(data)
print(sum(results[0]))
print(sum(results[1]))