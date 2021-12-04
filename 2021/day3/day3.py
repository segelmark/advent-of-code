validation = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".splitlines()

correctAnswer1 = 198
correctAnswer2 = 230

def count_instances(data, i):
    return sum(1 for line in data if line[i]=='1'), sum(1 for line in data if line[i]=='0')

def day1a(data):
    gamma=''
    epsilon=''
    count=[0] * len(data[0])
    for line in data:
        i=0
        while(i<(len(line))):
            count[i]+=int(line[i])
            i+=1

    for num in count:
        if num>len(data)/2:
            gamma+='1'
            epsilon+='0'
        else:
            epsilon+='1'
            gamma+='0'

    return int(gamma, 2) * int(epsilon, 2)

def oxygen(data):
    i=0
    while(i<(len(data[0]))):
        ones, zeros = count_instances(data, i)
        if(ones>=zeros):
            data=[line for line in data if line[i]=='1']
        else:
            data=[line for line in data if line[i]=='0']
        if(len(data)==1):
            break
        i+=1
    return(data[0])

def carbon(data):
    i=0
    while(i<(len(data[0]))):
        ones, zeros = count_instances(data, i)
        if(ones<zeros):
            data=[line for line in data if line[i]=='1']
        else:
            data=[line for line in data if line[i]=='0']
        if(len(data)==1):
            break
        i+=1
    return(data[0])

def day1b(data):
    o2=oxygen(data)
    co2=carbon(data)
    return int(o2,2)*int(co2,2)


# Make sure everything looks OK
assert day1a(validation) == correctAnswer1

f = open("input.txt", "r")
data = f.read().splitlines()

print(day1a(data))

# Make sure everything looks OK again
assert day1b(validation) == correctAnswer2

print(day1b(data))
