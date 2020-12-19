from validationdata import *


import collections
  
def pattern(seq):
        storage = {}
        for length in range(1,int(len(seq)/2)+1):
                valid_strings = {}
                for start in range(0,len(seq)-length+1):
                        valid_strings[start] = tuple(seq[start:start+length])
                candidates = set(valid_strings.values())
                if len(candidates) != len(valid_strings):
                        print("Pattern found for " + str(length))
                        storage = valid_strings
                else:
                        print("No pattern found for " + str(length))
                        break
        return set(v for v in storage.values() if list(storage.values()).count(v) > 1)

def play(start, until=2020):
    turn=1
    occurences={}
    for number in start: # initialize
        occurences[number]=[turn]
        turn+=1
    while turn<=until:
        #print(occurences[number])
        if not len(occurences.get(number))>1: # If that was the first time the number has been spoken
            number=0 # The current player says 0
        else: #Otherwise, the number had been spoken before
            number=turn-1-occurences[number][-2]# The current player announces how many turns apart the number is from when it was previously spoken.
        if occurences.get(number):
            occurences[number].append(turn)
        else:
            occurences[number]=[turn]
        #print(f"Turn: {turn} - Number: {number}")
        turn+=1
    return number

print(play([0,3,6], 10))

for v in validationdata:
    assert play(v[0]) == v[1]

import time

start = time.time()
number = play([7,12,1,0,16,2],30000000)

print(number)
end = time.time()
print(end - start)