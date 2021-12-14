validation1 = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf""".splitlines()
validation = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".splitlines()

correctAnswer1 = 26
correctAnswer2a = 5353
correctAnswer2b = 61229

original = ['abcefg','cf','acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
# original = ['cagedb', 'ab', 'gcdfa', 'gcdfa', 'eafb', 'cdfbe', 'cdfgeb', 'dab', 'acedgfb', 'cefabd']

# 1=cf, 4=bcdf, 7, 8

def day8(data):
    data = [ x.split(" | ") for x in data ]
    data = [[y.split() for y in x] for x in data]
    count=0

    for line in data:
        key = {}
        for segment in line:
            number=''
            for code in segment:
                if(len(code)==2): #1
                    key[1]=[c for c in code]
                    if(segment==line[1]):
                        count+=1
                        number+='1'
                elif(len(code)==4): #4
                    key[4]=[c for c in code]
                    if(segment==line[1]):
                        count+=1
                        number+='1'
                elif(len(code)==3): #7
                    key[7]=[c for c in code]
                    if(segment==line[1]):
                        count+=1
                        number+='7'
                elif(len(code)==7): #8
                    key[8]=[c for c in code]
                    if(segment==line[1]):count+=1
                elif(len(code)==5 and segment==line[1]):
                    if(key[1][0] in segment and key[1][1]):
                        number+='3'
                    
        correct={}
        for char in key[7]:
            if not char in key[1]:
                correct['a']=char
        new=[]
        for number in line[1]:
            for char, code in correct.items():
                number=number.replace(code, char)
            new.append(number)
        print(new)
        
        
            
    return count

# Make sure everything looks OK
# assert day8(validation) == correctAnswer1

print(day8(validation))

f = open("input.txt", "r")
data = f.read().splitlines()

# print(day8(data))

# Make sure everything looks OK again
# assert day8b(validation) == correctAnswer2
# print(day8b(validation))

# print(day8b(data))
