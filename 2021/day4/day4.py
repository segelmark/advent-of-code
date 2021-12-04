validation = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

correctAnswer1 = 4512
correctAnswer2 = 1924

def check_winner(board):
    for row in board:
        col=0
        for num in row:
            if(num!='X'):
                break
            col+=1
            if(col==len(board)):
                return True
    
    col=0
    while(col<len(board)):
        row=0
        while(row<len(board)):
            if(board[row][col]!='X'):
                break
            row+=1
            if(row==len(board)):
                return True
        col+=1
    return False

def count_unmarked(board):
    count=0
    for row in board:
        for num in row:
            if(num!='X'):
                count+=int(num)
    return count

def bingo(data, desired_position=999):
    data=data.split('\n\n')
    instructions=data[0].split(',')
    boards=data[1:]
    i=0
    for block in boards:
        boards[i]=block.splitlines()
        j=0
        for row in boards[i]:
            boards[i][j] = row.replace('  ', ' ').split()
            j+=1
        i+=1

    winners=[]
    for draw in instructions:
        i=0
        for board in boards:
            if not i in winners:
                y=0
                for row in board:
                    x=0
                    for number in row:
                        if(number)==draw:
                            boards[i][y][x]='X'
                            if(check_winner(boards[i])):
                                winners.append(i)
                                if(len(winners)==desired_position or len(winners)==len(boards)):
                                    return int(draw)*count_unmarked(boards[i])
                        x+=1
                    y+=1
            i+=1


# Make sure everything looks OK
assert bingo(validation, 1) == correctAnswer1

f = open("input.txt", "r")
data = f.read()

print(bingo(data, 1))

# Make sure everything looks OK again
assert bingo(validation) == correctAnswer2

print(bingo(data))
