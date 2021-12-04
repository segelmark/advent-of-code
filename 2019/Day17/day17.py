"""
2 is a block tile. Blocks can be broken by the ball.
3 is a horizontal paddle tile. The paddle is indestructible.
4 is a ball tile. The ball moves diagonally and bounces off objects. """
def render_map(map):
    for row in map:
        string=""
        for col in row:
            string+=col
        print(string)

def find_intersection(map):
    intersections=[]
    i=0
    for row in map:
        j=0
        for col in row:
            if(j>1 and i>1 and j<len(row)+1 and i<len(map)+1):
                if(map[i][j]=="#" and map[i][j-1]=="#" and map[i][j+1]=="#" and map[i-1][j]=="#" and map[i+1][j]=="#"):
                    map[i][j]="O"
                    intersections.append((i*j))

            j+=1
        i+=1
    return intersections, map

def get_parameters_modes(command):
    if(len(command)==1):
        return "0", "0", "0", "0"+command
    else:
        if(len(command)==2):
            return "0", "0", "0", command[-2:]
        else:
            if(len(command)==3):
                return "0", "0", command[-3],  command[-2:]
            else:
                if(len(command)==4):
                    return "0", command[-4], command[-3],  command[-2:]
                else:
                    return command[-5], command[-4], command[-3],  command[-2:]

def get_parameter(snippet, position, A,B,C, relative_base):
    if(C=="0"):
        param1=snippet[snippet[position+1]]
    else:
        if(C=="2"):
            param1=snippet[relative_base+snippet[position+1]]
        else:
            param1=snippet[position+1]
    if(B=="0"):
        param2=snippet[snippet[position+2]]
    else:
        if(B=="2"):
            param2=snippet[relative_base+snippet[position+2]]
        else:
            param2=snippet[position+2]
    if(A=="2"):
        param3=relative_base+snippet[position+3]
    else:
        param3=snippet[position+3]
    
    return param1, param2, param3

def get_param1(snippet, position, A,B,C, relative_base):
    if(C=="0"):
        param1=snippet[snippet[position+1]]
    else:
        if(C=="2"):
            param1=snippet[relative_base+snippet[position+1]]
        else:
            param1=snippet[position+1]
    
    return param1

def opcode5(snippet, position, A,B,C, relative_base):
    param1, param2, param3 = get_parameter(snippet, position, A,B,C, relative_base)
    if(param1):
        position=param2
    else:
        position=position+3
    return snippet, position

def opcode6(snippet, position, A,B,C, relative_base):
    param1, param2, param3 = get_parameter(snippet, position, A,B,C, relative_base)

    if(param1 == 0):
        position=param2
    else:
        position=position+3
    return snippet, position

def opcode7(snippet, position, A,B,C, relative_base):
    param1, param2, param3 = get_parameter(snippet, position, A,B,C, relative_base)

    if(param1<param2):
        snippet[param3]=1
    else:
        snippet[param3]=0
    position=position+4
    return snippet, position

def opcode8(snippet, position, A,B,C, relative_base):
    param1, param2, param3 = get_parameter(snippet, position, A,B,C, relative_base)

    if(param1==param2):
        snippet[param3]=1
    else:
        snippet[param3]=0
    position=position+4
    return snippet, position


def make_int_list(input_txt):
    string_array=input_txt.split(",")
    return [int(i) for i in string_array]

def Intcode(code1,part=0,debug=0):
    i=0
    while(i<10000):
        code1.append(0)
        i+=1
    dim=61
    position={"x":32,"y":0}
    canvas=[[" " for i in range(dim)] for i in range(dim)]
    relative_base=0
    code=list(code1)
    if part!=0:
        code[0]=part
    output=""
    line=0
    column=0
    i=0
    while(i<len(code)):
        command=str(code[i])
        if(debug==1):
            print("Position: "+str(i))
            print("Command: "+ str(command))
        A, B, C, DE = get_parameters_modes(command)
        if(DE=="01"):
            param1, param2, param3 = get_parameter(code, i, A,B,C, relative_base)
            code[param3]=param1+param2
            i+=4
        else:
            if(DE=="02"): 
                param1, param2, param3 = get_parameter(code, i, A,B,C, relative_base)
                code[param3]=param1*param2
                i+=4
            else:
                if(DE=="03"): 
                    param1=get_param1(code, i, A,B,C, relative_base)
                    # render_map(canvas)
                    A_code="R,4,R,12,R,10,L,12\n"
                    B_code="L,12,R,4,R,12\n"
                    C_code="L,12,L,8,R,10\n"
                    inst_code="A,B,B,C,C,A,B,B,C\n"
                    n_code="n\n"
                    test=''.join(str(ord(c)) for c in inst_code)+''.join(str(ord(c)) for c in A_code)+''.join(str(ord(c)) for c in B_code)+''.join(str(ord(c)) for c in C_code)+''.join(str(ord(c)) for c in n_code)
                    print(test)
                    print('Inst: '+''.join(str(ord(c)) for c in inst_code) +'10')
                    print('A: '+''.join(str(ord(c)) for c in A_code) +'10')
                    print('B: '+''.join(str(ord(c)) for c in B_code) +'10')
                    print('C: '+''.join(str(ord(c)) for c in C_code) +'10')
                    print('y/n: '+''.join(str(ord(c)) for c in n_code) +'10')
                    user_input=int(input())
                                   
                    if(C=="2"):
                        code[relative_base+code[i+1]]=user_input
                    else:
                        code[code[i+1]]=user_input
                    i+=2
                else:
                    if(DE=="04"):
                        param1=get_param1(code, i, A,B,C, relative_base)
                        if(part==1):
                            if(param1==10):
                                column=0
                                line+=1
                            else:
                                canvas[line][column]=chr(param1)
                                column+=1
                        print(chr(param1))
                        i+=2
                    else:
                        if(DE=="05"): 
                            code, i = opcode5(code,i,A,B,C,relative_base)
                        else:
                            if(DE=="06"): 
                                code, i = opcode6(code,i,A,B,C,relative_base)
                            else:
                                if(DE=="07"): 
                                    code, i = opcode7(code,i,A,B,C,relative_base)
                                else:
                                    if(DE=="08"): 
                                        code, i = opcode8(code,i,A,B,C,relative_base)
                                    else:
                                        if(DE=="09"): 
                                            param1=get_param1(code, i, A,B,C, relative_base)
                                            relative_base=relative_base+param1
                                            i+=2
                                        else:
                                            if(DE=="99"):
                                                if(part==1):
                                                    intersections, canvas=find_intersection(canvas)
                                                    render_map(canvas)
                                                    print(sum(intersections))
                                                    A="R4R12R10L12"
                                                    B="L12R4R12"
                                                    C="L12L8R10"
                                                    input_str=A+B+B+C+C+A+B+B+C # "R4R12R10L12L12R4R12L12R4R12L12L8R10L12L8R10R4R12R10L12L12R4R12L12R4R12L12L8R10"
                                                    move_robot(canvas, position, input_str)
                                                return canvas
                                            else:
                                                print("ERROR")
                                                return [None]

def move(canvas, position, direction, steps):
    print("Move: "+ str(steps) + " in direction: " + str(direction))
    step=0
    value=position["y"]*position["x"]
    while(step<steps):
        canvas[position["y"]][position["x"]]="X"
        if(direction==0):
            position["y"]-=1
            dir_char="^"
        elif(direction==1):
            position["x"]+=1
            dir_char=">"
        elif(direction==2):
            position["y"]+=1
            dir_char="v"
        elif(direction==3):
            position["x"]-=1
            dir_char="<"
        canvas[position["y"]][position["x"]]=dir_char
        step+=1
        value+=position["y"]*position["x"]
    render_map(canvas)
    input()
    return canvas,value

def move_robot(canvas, position, instructions):
    direction=0
    sum=0
    step=0
    while(step<len(instructions)):
        if(instructions[step]=="R"):
            direction=(direction+1)%4
            step+=1
        elif(instructions[step]=="L"):
            direction=(direction-1)%4
            step+=1
        else:
            if(step+1<len(instructions)):
                if(instructions[step+1]!="R" and instructions[step+1]!="L"):
                    canvas, value=move(canvas, position, direction, int(instructions[step:step+2]))
                    sum+=value
                    step+=2
                    continue
            canvas, value=move(canvas, position, direction, int(instructions[step]))
            step+=1
            sum+=value
    print(sum)

filename = "Day17/input.txt"
file = open(filename, "r")
input_txt=file.readline()
input_txt=make_int_list(input_txt)

maze_map=Intcode(input_txt,1,0)

