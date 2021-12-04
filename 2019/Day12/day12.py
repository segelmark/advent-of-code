def apply_gravity(moons, i):
    a=0
    while(a<len(moons)):
        moon=moons[a]
        b=a+1
        while(b<len(moons)):
            other_moon=moons[b]
            if(moon["pos"][i]<other_moon["pos"][i]):
                moon["velocity"][i]+=1
                other_moon["velocity"][i]-=1
            if(moon["pos"][i]>other_moon["pos"][i]):
                moon["velocity"][i]-=1
                other_moon["velocity"][i]+=1
            b+=1
        a+=1

    return moons

def apply_velocity(moons,i):
    for moon in moons:
        moon["pos"][i]+=moon["velocity"][i]
    return moons

def potential_energy(moon):
    return abs(moon["pos"][0])+abs(moon["pos"][1])+abs(moon["pos"][2])

def kinetic_energy(moon):
    return abs(moon["velocity"][0])+abs(moon["velocity"][1])+abs(moon["velocity"][2])

def total_energy(moons):
    total_energy=0
    for moon in moons:
        print("Pot: "+str(potential_energy(moon)))
        print("Kin: "+str(kinetic_energy(moon)))
        total_energy+=potential_energy(moon)*kinetic_energy(moon)
    return total_energy

def time_step(moons,i):
    moons=apply_gravity(moons,i)
    moons=apply_velocity(moons,i)
    return moons

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)


# moons=[{"pos":[-1, 0, 2], "velocity":[0,0,0]}, {"pos":[2, -10, -7], "velocity":[0,0,0]}, {"pos":[4,-8,8], "velocity":[0,0,0]}, {"pos":[3,5,-1], "velocity":[0,0,0]}]
# moons=[{"pos":[-8, -10, 0], "velocity":[0,0,0]}, {"pos":[5, 5, 10], "velocity":[0,0,0]}, {"pos":[2,-7,3], "velocity":[0,0,0]}, {"pos":[9,-8,-3], "velocity":[0,0,0]}]
moons = [{"pos":[-3, 15, -11], "velocity":[0,0,0]}, {"pos":[3, 13, -19], "velocity":[0,0,0]}, {"pos":[-13,18,-2], "velocity":[0,0,0]}, {"pos":[6,0,-1], "velocity":[0,0,0]}]
import copy
org_moons=copy.deepcopy(moons)
print(moons)
import time
start_time = time.time()
den=[]
dimension=0
while(dimension<3):
    i=0
    while(i<10000000):
        moons=time_step(moons,dimension)
        if(moons[0]["velocity"][dimension]==0 and moons[1]["velocity"][dimension]==0 and moons[2]["velocity"][dimension]==0 and moons[3]["velocity"][dimension]==0):
            if(moons[0]["pos"][dimension]==org_moons[0]["pos"][dimension] and moons[1]["pos"][dimension]==org_moons[1]["pos"][dimension] and moons[2]["pos"][dimension]==org_moons[2]["pos"][dimension] and moons[3]["pos"][dimension]==org_moons[3]["pos"][dimension]):
                den.append(i+1)
                print(i+1)
                break
        i+=1
    dimension+=1
print("--- %s seconds ---" % (time.time() - start_time))

print(int(lcm(lcm(den[0], den[1]), den[2])))
