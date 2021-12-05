validation = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".splitlines()

correctAnswer1 = 5
correctAnswer2 = 12

def renderBoard(board):
    for line in board:
        print(line)

def draw(line,board,include_diagonal):
    [ x1, y1, x2, y2 ] = line
    x, y = x1, y1

    delta_x,delta_y = 1,1
    if(x1>x2): delta_x = -1
    if(y1>y2): delta_y = -1

    if x1 == x2 and not y1 == y2:
        while(y!=y2+delta_y):
            board[y][x]=board[y][x]+1
            y+=delta_y

    elif y1 == y2 and not x1 == x2:
        while(not x==x2+delta_x):
            board[y][x]=board[y][x]+1
            x+=delta_x

    elif include_diagonal and not x1 == x2 and not y1 == y2:
        while(x!=x2+delta_x):
            board[y][x]=board[y][x]+1
            y+=delta_y
            x+=delta_x

    return board

def countIntersections(board):
    count=0
    for line in board:
        for point in line:
            if point>1:
                count+=1
    return count

def day5(data,n=10,include_diagonal=False,render=False):
    data = [x.replace(" -> ",",").split(",") for x in data]
    data = [[int(y) for y in x] for x in data]

    board = [ [ 0 for i in range(n) ] for j in range(n) ]

    for line in data:
        board = draw(line, board, include_diagonal)
        if(render):
            renderBoard(board)

    return countIntersections(board)

# Make sure everything looks OK
assert day5(validation) == correctAnswer1

f = open("input.txt", "r")
data = f.read().splitlines()

print(day5(data,1000))

# Make sure everything looks OK again
assert day5(validation,10,True) == correctAnswer2

print(day5(data,1000,True))
