validation="389125467"
puzzle_input="789465123"

def playGame(data, moves=100, cup_qty=9):
    cups = [int(c) for c in data]
    if cup_qty>len(cups):
        cups += list(range(10, 1000001))
    print(cups[-1])
    length=len(cups)
    current_cup=cups[0]
    pickup=[]
    for move in range(1,moves+1):
        current_index=cups.index(current_cup)
        pickup=(cups*3)[(current_index+1):(current_index+4)]
        destination=current_cup-1
        if destination<1:
            destination=length
        while destination in pickup:
            destination-=1
            if destination<1:
                destination=length
        #print(f"""-- Move {move} --
        #cups: {cups} -> {current_cup}
        #pick up: {pickup}
        #destination: {destination}""")
        for cup in pickup:
            cups.remove(cup)
        for i, cup in enumerate(pickup):
            cups.insert((cups.index(destination)+1+i)%length,cup)
        current_cup=cups[(cups.index(current_cup)+1)%length]
    if(cup_qty==9):
        return ''.join(str(x) for x in (cups[cups.index(1):]+cups[:cups.index(1)])[1:])
    else:
        return cups[cups.index(1)-1]*cups[cups.index(1)-2]
        



assert playGame(validation,10) == "92658374"
assert playGame(validation,100) == "67384529"

print(playGame(validation,10000000,1000000))

# print(playGame(puzzle_input,100))

"""-- move 1 --
cups: (3) 8  9  1  2  5  4  6  7 
pick up: 8, 9, 1
destination: 2

-- move 2 --
cups:  3 (2) 8  9  1  5  4  6  7 
pick up: 8, 9, 1
destination: 7

-- move 3 --
cups:  3  2 (5) 4  6  7  8  9  1 
pick up: 4, 6, 7
destination: 3

-- move 4 --
cups:  7  2  5 (8) 9  1  3  4  6 
pick up: 9, 1, 3
destination: 7

-- move 5 --
cups:  3  2  5  8 (4) 6  7  9  1 
pick up: 6, 7, 9
destination: 3

-- move 6 --
cups:  9  2  5  8  4 (1) 3  6  7 
pick up: 3, 6, 7
destination: 9

-- move 7 --
cups:  7  2  5  8  4  1 (9) 3  6 
pick up: 3, 6, 7
destination: 8

-- move 8 --
cups:  8  3  6  7  4  1  9 (2) 5 
pick up: 5, 8, 3
destination: 1

-- move 9 --
cups:  7  4  1  5  8  3  9  2 (6)
pick up: 7, 4, 1
destination: 5

-- move 10 --
cups: (5) 7  4  1  8  3  9  2  6 
pick up: 7, 4, 1
destination: 3

-- final --
cups:  5 (8) 3  7  4  1  9  2  6"""