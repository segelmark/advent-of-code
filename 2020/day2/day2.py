validation = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".splitlines()


def day2(data, rule):
    """ Checks how many times the given rule is valid in the data """
    passwords = [l.replace(':','').replace('-', ' ').split() for l in data]
    count=0
    for [pos1, pos2, char, password] in passwords:
        if(rule(pos1, pos2, char, password)):
            count=count+1
    return count

def rule1([pos1, pos2, char, password]):
    if(password.count(char)<=int(pos2) and password.count(char)>=int(pos1)):
        return True

def rule2(pos1, pos2, char, password):
    val1=password[int(pos1)-1]
    val2=password[int(pos2)-1]
    if(bool(val1==char) ^ bool(val2==char)):
        return True


assert(day2(validation, rule1) == 2)

f = open("input.txt", "r")
data = f.read().splitlines()

print(day2(data, rule1))


assert(day2(validation, rule2) == 1)


print(day2(data, rule2))
