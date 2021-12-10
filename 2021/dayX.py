validation = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".splitlines()

correctAnswer1 = 5
#correctAnswer2 = 5

def dayX(data):
    # data = [int(x) for x in data]
    # data = [x.split() for x in data]
    # data = [x.replace(" -> ",",").split(",") for x in data]
    # data = [[int(y) for y in x] for x in data]

    count=0
    i=1
    while(i<(len(data))):
        if(data[i]>data[i-1]):
            count+=1
        i=i+1
    return count

# Make sure everything looks OK
# assert dayX(validation) == correctAnswer1

print(dayX(validation))

f = open("input.txt", "r")
data = f.read().splitlines()

# print(dayX(data))

# Make sure everything looks OK again
# assert dayXb(validation) == correctAnswer2
# print(dayXb(validation))

# print(dayXb(data))
