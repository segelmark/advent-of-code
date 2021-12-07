validation = """16,1,2,0,4,2,7,1,2,14"""

correctAnswer1 = 37
correctAnswer2 = 168

def align_to(pos,data,costly):
    count=0
    for num in data:
        if not costly:
            count+=abs(num-pos)
        else:
            count+=(abs(num-pos)**2+abs(num-pos))/2
    return count

def day7(data,costly=False):
    data = [int(x) for x in data.split(",")]
        
    min=9223372036854775807 #max int
    i=0
    latest=0
    while(latest<=min):
        latest=align_to(i,data,costly)
        if latest<min:
            min=latest
        i+=1
    return min
    
# Make sure everything looks OK
assert day7(validation) == correctAnswer1

f = open("input.txt", "r")
data = f.read()

print(day7(data))

# Make sure everything looks OK again
assert day7(validation,costly=True) == correctAnswer2

print(day7(data,costly=True))
