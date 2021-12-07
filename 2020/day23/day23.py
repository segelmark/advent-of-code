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
