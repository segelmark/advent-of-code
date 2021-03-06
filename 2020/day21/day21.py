from validationdata import *

def parseData(data):
    return [ [f[0].split(" "), f[1].split(", ")] for f in [line.replace(")","").split(" (contains ") for line in data]]

def overlapAllergens(food_list):
    allergens={}
    for food in food_list:
        for allergen in food[1]:
            if not allergen in allergens:
                allergens[allergen]=food[0]
                # print(f"{allergen}: {allergens[allergen]}")
            else:
                save=[]
                for ingredient in food[0]:
                    if ingredient in allergens[allergen]:
                        save.append(ingredient)
                allergens[allergen]=save
    return allergens

def uniqueFoodsPerAllergen(allergens):
    unique={}
    i=0
    while i<=len(allergens):
        for allergen, ingredients in allergens.items():
            if(len(ingredients)==1):
                unique[allergen]=ingredients[0]
                for key, val in allergens.items():
                    if(len(val)>1):
                        try:
                            val.remove(ingredients[0])
                        except:
                            pass
        i+=1
    return unique

f = open("input.txt", "r")
data = f.read().splitlines()

""" Part 1 """

food_list=parseData(data)
allergens=overlapAllergens(food_list)
print(allergens)
avoid=uniqueFoodsPerAllergen(allergens)
print(avoid)

count=0
for item in food_list:
    for ingredient in item[0]:
        if not ingredient in avoid.values():
            count+=1
print(count)

""" Part 2 """

sorted=sorted(avoid.items())

output=""
for s in sorted:
    output+=s[1]+","
print(output.strip(","))