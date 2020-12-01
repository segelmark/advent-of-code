validation1 = """1721
979
366
299
675
1456"""

validation2 = """1235
979
366
675
299
1721""" 

correctAnswer1=514579
correctAnswer2=241861950

def day1(input):
    i=0
    j=0
    while(i<(len(input)-1)):
        j=i+1
        while(j<len(input)):
            # print(input[i] + " + " + input[j] + " = " + str(int(input[i])+int(input[j])))
            if(int(input[i])+int(input[j])==2020):
                print(input[i] + " + " + input[j] + " = " + str(int(input[i])+int(input[j])))
                return int(input[j])*int(input[i])
            j=j+1
        i=i+1

def day2(input):
    i=0
    j=0
    k=0
    while(i<(len(input)-2)):
        j=i+1
        while(j<len(input)-1):
            k=j+1
            while(k<len(input)):
                # print(input[i] + " + " + input[j] + " = " + str(int(input[i])+int(input[j])))
                if(int(input[i])+int(input[j])+int(input[k])==2020):
                    print(input[i] + " + " + input[j] + " + " + input[k] + " = " + str(int(input[i])+int(input[j])+int(input[k])))
                    return int(input[i])*int(input[j])*int(input[k])
                k=k+1
            j=j+1
        i=i+1

# Make sure everything look OK
assert day1(validation1.splitlines()) == correctAnswer1
assert day1(validation2.splitlines()) == correctAnswer1

f = open("input.txt", "r")
data = f.read().splitlines()

print(day1(data))

# Make sure everything look OK again
assert day2(validation1.splitlines()) == correctAnswer2
assert day2(validation2.splitlines()) == correctAnswer2

print(day2(data))