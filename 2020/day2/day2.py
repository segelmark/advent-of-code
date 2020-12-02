validation = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".splitlines()



def day2a(data):
    passwords = [l.replace(':','').replace('-', ' ').split() for l in data]
    count=0
    for [min, max, char, password] in passwords:
        # print(f"{min} {max} {char} {password}")
        if(password.count(char)<=int(max) and password.count(char)>=int(min)):
            count=count+1
    return count

assert(day2a(validation) == 2)

f = open("input.txt", "r")
data = f.read().splitlines()

print(day2a(data))

def day2b(data):
    passwords = [l.replace(':','').replace('-', ' ').split() for l in data]
    count=0
    for [pos1, pos2, char, password] in passwords:
        val1=password[int(pos1)-1]
        print(val1)
        val2=password[int(pos2)-1]
        print(val2)
        if(bool(val1==char) ^ bool(val2==char)):
            count=count+1
    return count

assert(day2b(validation) == 1)


print(day2b(data))
