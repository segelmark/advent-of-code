validation = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

correctAnswer1 = 17
#correctAnswer2 = 5

def fold(dots,dir,pos):
    for i in range(len(dots)):
        if(dir=='y' and dots[i][1]>pos):
            dots[i][1]=abs(2*pos-dots[i][1])
        elif(dir=='x' and dots[i][0]>pos):
            dots[i][0]=abs(2*pos-dots[i][0])
    return dots



def dayX(data):
    data=data.split('\n\n')
    dots=[[int(y) for y in x.split(',')] for x in data[0].splitlines()]
    instructions=[[x.replace('fold along ','').split('=')[0], int(x.split('=')[1]) ] for x in data[1].splitlines()]

    for inst in instructions:
    # inst = instructions[0]
        dots=fold(dots,inst[0],inst[1])

    page=[['.' for x in range(40)] for y in range(40)]
    
    dot_set=set()
    for dot in dots:
        page[dot[0]][dot[1]]='X'
        dot_set.add((dot[0],dot[1]))
    for line in page:
        print(''.join(line))

    print(sorted(dot_set))

    return len(dot_set)

# Make sure everything looks OK
# assert dayX(validation) == correctAnswer1

print(dayX(validation))

f = open("input.txt", "r")
data = f.read()

print(dayX(data))

# Make sure everything looks OK again
# assert dayXb(validation) == correctAnswer2
# print(dayXb(validation))

# print(dayXb(data))
