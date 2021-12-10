validation = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".splitlines()

correctAnswer1 = 26397
correctAnswer2 = 288957

scorer ={ ')': 3, ']': 57, '}': 1197, '>': 25137 }
scorer2 ={ ')': 1, ']': 2, '}': 3, '>': 4 }
replacer ={ '(':')', '[':']', '{':'}', '<':'>'}

def dayX(data):
    invalids={ ')': 0, ']': 0, '}': 0, '>': 0 }
    complete_lines=[]

    for line in data:
        last_open=[]
        complete=True
        for char in line:
            if(char in ['(', '[', '{', '<']):
                last_open.append(replacer[char])
            elif(char in [')', ']', '}', '>']):
                if last_open.pop()!=char:
                    invalids[char]+=1
                    complete=False
                    break
        if(complete):
            last_open.reverse()
            complete_lines.append(last_open)

    #part 1
    score = scorer[')']*invalids[')']+scorer[']']*invalids[']']+scorer['}']*invalids['}']+scorer['>']*invalids['>']
    
    #part 2
    scores=[]
    for line in complete_lines:
        line_score=0
        for char in line:
            line_score=line_score*5+scorer2[char]
        scores.append(line_score)
    
    score2=sorted(scores)[len(scores)/2]

    return (score, score2)

# Make sure everything looks OK
assert dayX(validation) == (correctAnswer1, correctAnswer2)

f = open("input.txt", "r")
data = f.read().splitlines()

print(dayX(data))