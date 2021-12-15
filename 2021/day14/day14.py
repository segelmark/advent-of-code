import copy

validation = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

correctAnswer1 = 1588
correctAnswer2 = 2188189693529

def day14(data,iterations=40):
    data=data.split('\n\n')
    template=data[0]
    rules=[x.split(' -> ') for x in data[1].splitlines()]
    # data = [int(x) for x in data]
    # data = [x.split() for x in data]
    # data = [x.replace(" -> ",",").split(",") for x in data]
    # data = [[int(y) for y in x] for x in data]

    
    empty_count=dict()
    for rule in rules:
        empty_count[rule[0]]=0
    pair_count=empty_count
    for i in range(len(template)-1):
        pair_count[template[i]+template[i+1]]+=1
    for j in range(iterations):
        new=copy.deepcopy(pair_count)
        for rule in rules:
            new[rule[0]]-=pair_count[rule[0]]
            new[rule[0][0]+rule[1]]+=pair_count[rule[0]]
            new[rule[1]+rule[0][1]]+=pair_count[rule[0]]
        pair_count=new

    all_freq = {}
    for pair in pair_count:
        all_freq[pair[0]]=all_freq.get(pair[0],0)+pair_count[pair]
        all_freq[pair[1]]=all_freq.get(pair[1],0)+pair_count[pair]

    all_values = all_freq.values()
    max_value = max(all_values)
    min_value = min(all_values)

    max_key = max(all_freq, key=all_freq.get)
    if max_key==template[0]:
        max_value+=1
    if max_key==template[-1]:
        max_value+=1

    
    min_key = min(all_freq, key=all_freq.get)
    if min_key==template[0]:
        min_value+=1
    if min_key==template[-1]:
        min_value+=1


    return (max_value-min_value)/2


# Make sure everything looks OK
assert day14(validation,10) == correctAnswer1

f = open("input.txt", "r")
data = f.read()

print(day14(data,10))

# Make sure everything looks OK again
assert day14(validation,40) == correctAnswer2

print(day14(data,40))
