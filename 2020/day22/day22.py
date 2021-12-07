from validationdata import *

def parseData(data):
    return [[int(card) for card in player.splitlines()[1:]]
     for player in data.split("\n\n")]

def countScore(input):
    player_cards,winner = input
    sum = 0
    for i, card in enumerate(player_cards[winner-1]):
        sum += card*(len(player_cards[winner-1])-i)
    return sum

def playRound(player_cards,recursive=False):
    p1 = player_cards[0].pop(0)
    p2 = player_cards[1].pop(0)
    if recursive and p1<= len(player_cards[0]) and p2 <= len(player_cards[1]):
        winner = combat([player_cards[0][:p1].copy(),player_cards[1][:p2]].copy(),True)[1]
    elif(p1>p2):
        winner = 1
    else:
        winner = 2
    if winner == 1:
        player_cards[0] += [p1, p2]
    else:
        player_cards[1] += [p2, p1]
    return player_cards, winner

def combat(player_cards,recursive=False):
    round = 1
    historic = set()
    while player_cards[0] and player_cards[1]:
        if (state := (tuple(player_cards[0]), tuple(player_cards[1]))) in historic:
            return player_cards, 1
        historic.add(state)
        player_cards, winner = playRound(player_cards,recursive)
        round += 1
    return player_cards, winner

assert countScore(combat(parseData(validationdata))) == 306

assert countScore(combat(parseData(validationdata),True, True)) == 291

assert combat(parseData(validation2),True)[1] == 1

f = open("input.txt", "r")
data = f.read()

for recursive in False, True:
    print(countScore(combat(parseData(data),recursive)))