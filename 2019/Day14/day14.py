inventory={}

def make(substance, required, formulas):
    global inventory
    
    # get batches to produce
    import math
    batches = int(math.ceil(required/int(formulas[substance]["qty"])))

    # create the new substance in the right batch quantities
    if substance in inventory:
        inventory[substance]+=int(formulas[substance]["qty"])*batches
    else:
        inventory[substance]=int(formulas[substance]["qty"])*batches
    
    # consume resources required
    if(formulas[substance]["inputs"][0][1]=="ORE"):
        return int(formulas[substance]["inputs"][0][0])*batches
    else:
        ore_required=0
        for ingredient in formulas[substance]["inputs"]:
                required_of_ingredient=int(ingredient[0])*batches

                #if we have ingredients in inventory we do not have to make new
                if ingredient[1] in inventory:
                    if(inventory[ingredient[1]]>=required_of_ingredient):
                        inventory[ingredient[1]]-=required_of_ingredient
                        continue
                    else:
                        required_of_ingredient-=inventory[ingredient[1]]
                        inventory[ingredient[1]]=0

                # if we do not have enoigh in inventory
                ore_required+=int(make(ingredient[1], required_of_ingredient, formulas))
                inventory[ingredient[1]]-=required_of_ingredient

        return ore_required

def get_inputs(inputs):
    processed_inputs=[]
    for inp in inputs:
        processed_inputs.append(inp.split(" "))
    return processed_inputs

filename = "Day14/input.txt"
file = open(filename, "r")
formulas={}

for line in file:
    before_after=line[:-1].split(" => ")
    output=before_after[1].split(" ")
    inputs=get_inputs(before_after[0].split(", "))
    formulas[output[1]]={"qty":output[0], "inputs": inputs}

import time
start_time = time.time()

inventory={}
fuel=int(10**12/make("FUEL", 1, formulas)*1.5)
print("Starting at: "+str(fuel))
print("--- %s seconds ---" % (time.time() - start_time))
i=5
while(i>=0):
    if(i!=5):
        fuel-=10**(i+1)
    inventory={}
    ore_required=make("FUEL", fuel, formulas)
    while(ore_required<10**12):
        fuel+=10**i
        inventory={}
        ore_required=make("FUEL", fuel, formulas)
    i=i-1
fuel-=1        
print(fuel)
print(make("FUEL", fuel, formulas))

print("--- %s seconds ---" % (time.time() - start_time))

