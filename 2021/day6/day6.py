validation = """3,4,3,1,2"""

correctAnswer1 = 5934
correctAnswer2 = 26984457539

def day6(data,end=80):
    fishes = [int(x) for x in data.split(",")]
    fishy={}
    for num in range(0,9):
        fishy[num]=fishes.count(num)

    d=0

    while(d<end):
        new_fishes=fishy[0]
        i=1
        while(i<=8):
            fishy[i-1]=fishy[i]
            i+=1
        d+=1
        fishy[6]+=new_fishes
        fishy[8]=new_fishes

    total=0
    for num in range(0,9):
        total+=fishy[num]

    return total

# Make sure everything looks OK
assert day6(validation) == correctAnswer1

f = open("input.txt", "r")
data = f.read()

print(day6(data))

# Make sure everything looks OK again
assert day6(validation,256) == correctAnswer2

print(day6(data,256))
