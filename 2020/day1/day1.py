import time

start = time.time()

validation1 = """1721
979
366
299
675
1456""".splitlines()

validation2 = """1235
979
366
675
299
1721""".splitlines()

correctAnswer1=514579
correctAnswer2=241861950

def day1(data):
    data = [int(x) for x in data]
    i=0
    j=0
    while(i<(len(data)-1)):
        j=i+1
        while(j<len(data)):
            if(data[i]+data[j]==2020):
                print(f"{data[i]} + {data[j]} = {data[i]+data[j]}")
                return data[j]*data[i]
            j=j+1
        i=i+1

def day1b(data):
    data = [int(x.strip()) for x in data]
    i=0
    j=0
    k=0
    while(i<(len(data)-2)):
        j=i+1
        while(j<len(data)-1):
            k=j+1
            while(k<len(data)):
                if(data[i]+data[j]+data[k]==2020):
                    print(f"{data[i]} + {data[j]} + {data[k]} = {data[i]+data[j]+data[k]}")
                    return data[i]*data[j]*data[k]
                k=k+1
            j=j+1
        i=i+1

# Make sure everything look OK
assert day1(validation1) == correctAnswer1
assert day1(validation2) == correctAnswer1

f = open("input.txt", "r")
data = f.read().splitlines()

print(day1(data))

# Make sure everything look OK again
assert day1b(validation1) == correctAnswer2
assert day1b(validation2) == correctAnswer2

print(day1b(data))

end = time.time()
print(end - start)