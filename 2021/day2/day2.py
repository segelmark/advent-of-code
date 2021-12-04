validation = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".splitlines()

correctAnswer1 = 150
correctAnswer2 = 900

def initial_logic(data, horizontal=0, depth=0):
    for action in data:
        if action[0] == "forward":
            horizontal+=int(action[1])
        if action[0] == "up":
            depth-=int(action[1])
        if action[0] == "down":
            depth+=int(action[1])
        # print(action[0] + " " + action[1] + " to: " + str(horizontal) + " " + str(depth))
    return horizontal, depth

def aim_logic(data, horizontal=0, depth=0, aim=0):
    for action in data:
        if action[0] == "forward":
            horizontal+=int(action[1])
            depth+=aim*int(action[1])
        if action[0] == "up":
            aim-=int(action[1])
        if action[0] == "down":
            aim+=int(action[1])
        # print(action[0] + " " + action[1] + " to: " + str(horizontal) + " " + str(depth))
    return horizontal, depth

def day2(data, part=1):
    data = [x.split() for x in data]
    if(part==1):
        horizontal, depth =initial_logic(data)
    else:
        horizontal, depth =aim_logic(data)
    return horizontal*depth

# Make sure everything looks OK
assert day2(validation) == correctAnswer1

f = open("input.txt", "r")
data = f.read().splitlines()

print(day2(data))

# Make sure everything looks OK again
assert day2(validation,2) == correctAnswer2

print(day2(data,2))
