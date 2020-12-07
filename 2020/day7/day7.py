from validationdata import *

def count_if(data,bagcolor):
    relevantBags=set()
    for line in data:
        rule = line.split(" bags contain ")
        if bagcolor in rule[1]:
            relevantBags.add(rule[0])
            more_bags=count_if(data,rule[0])
            for bag in more_bags:
                relevantBags.add(bag)
    return relevantBags

assert len(count_if(validation,"shiny gold"))==4

def count_contents(data,bagcolor):
    count=0
    for line in data:
        rule = line.split(" bags contain ")
        if rule[0]==bagcolor:
            if rule[1]=="no other bags.":
                return 0
            contents=rule[1].replace("bags","bag").strip(" bag.").split(" bag, ")
            for content in contents:
                num=content[0]
                bag=content[2:]
                count+=int(num)
                count+=int(num)*count_contents(data,bag)
    return count

assert count_contents(validation,"shiny gold")==32

f = open("input.txt", "r")
data = f.read().splitlines()
relevant_bags=count_if(data,"shiny gold")
# print(relevant_bags)
print(len(relevant_bags))
print(count_contents(data,"shiny gold"))