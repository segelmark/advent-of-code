filename = "Day6/input.txt"
file = open(filename, "r")

dict = {}
parent_list = {}
for line in file:
    item=line.split(")")
    if(item[0] in dict):
        dict[item[0]].append(item[1][:-1])
    else:
        dict[item[0]]=[ item[1][:-1] ]
    parent_list[item[1][:-1]]=item[0]

def look_for(what,i):
    if(what in dict):
        i+=1
        count=i-1
        for line in dict[what]:
            count+=look_for(line,i)
        return count
    else:
        return i
print("Total orbits: " + str(look_for("COM",0)))

def find_path(planet,parent_list):
    if(planet=="COM"):
        return []
    else:
        path=find_path(parent_list[planet],parent_list)
        path.append(parent_list[planet])
        return path

def UniqueElements(li1, li2): 
    s2 = set(li2)
    s1 = set(li1)
    u = [x for x in li1 if x not in s2]
    v = [x for x in li2 if x not in s1]
    return u + v
  
# Driver Code 
path_you = find_path("YOU",parent_list)
path_you.reverse()
path_san = find_path("SAN",parent_list)
travel_path=UniqueElements(path_you, path_san)

print(travel_path)
print("Distance to travel: " + str(len(travel_path)))