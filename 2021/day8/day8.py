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

# 1=cf, 4=bcdf, 7, 8

def day8(data):
    data = [ x.split(" | ") for x in data ]
    data = [[y.split() for y in x] for x in data]
    count=0

    for line in data:
        key = {}
        for segment in line:
            for code in segment:
                if(len(code)==2): #1
                    key[code[0]]=original[1][0]
                    key[code[1]]=original[1][1]
                    count+=1
                elif(len(code)==4): #4
                    key[code[0]]=original[4][0]
                    key[code[1]]=original[4][1]
                    key[code[2]]=original[4][2]
                    key[code[3]]=original[4][3]
                    count+=1
                elif(len(code)==3): #7
                    key[code[0]]=original[7][0]
                    key[code[1]]=original[7][1]
                    key[code[2]]=original[7][2]
                    count+=1
                elif(len(code)==7): #8
                    key[code[0]]=original[8][0]
                    key[code[1]]=original[8][1]
                    key[code[2]]=original[8][2]
                    key[code[3]]=original[8][3]
                    key[code[4]]=original[8][4]
                    key[code[5]]=original[8][5]
                    key[code[6]]=original[8][6]
                    count+=1
        new=[]
        for number in line[1]:
            for char, code in key.items():
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
