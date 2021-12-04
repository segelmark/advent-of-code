validation = """199
200
208
210
200
207
240
269
260
263
""".splitlines()

correctAnswer1 = 7
correctAnswer2 = 5

def day1(data):
    data = [int(x) for x in data]
    count=0
    i=1
    while(i<(len(data))):
        if(data[i]>data[i-1]):
            count+=1
        i=i+1
    return count

def day1b(data):
    data = [int(x) for x in data]
    count=0
    i=1
    while(i<(len(data)-2)):
        if(data[i]+data[i+1]+data[i+2]>data[i-1]+data[i]+data[i+1]):
            count+=1
        i=i+1
    return count

# Make sure everything looks OK
assert day1(validation) == correctAnswer1

f = open("input.txt", "r")
data = f.read().splitlines()

print(day1(data))

# Make sure everything looks OK again
assert day1b(validation) == correctAnswer2

print(day1b(data))
