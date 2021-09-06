"""
2 is a block tile. Blocks can be broken by the ball.
3 is a horizontal paddle tile. The paddle is indestructible.
4 is a ball tile. The ball moves diagonally and bounces off objects. """
def render_map(map):
    count=0
    for row in map:
        string=""
        for col in row:
            if col == " " or col == "#" or col == "D" or col == "O":
                string+=str(col)
            else:
                string+="."
        print(string)

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

def get_direction(direction, position, canvas):
    if(canvas[position["y"]-1][position["x"]]==" "):
        return 1
    elif(canvas[position["y"]+1][position["x"]]==" "):
        return 2
    elif(canvas[position["y"]][position["x"]-1]==" "):
        return 3
    elif(canvas[position["y"]][position["x"]+1]==" "):
        return 4
    else:
        if(canvas[position["y"]-1][position["x"]]!="#" and canvas[position["y"]-1][position["x"]]!="X"):
            return 1
        elif(canvas[position["y"]+1][position["x"]]!="#" and canvas[position["y"]+1][position["x"]]!="X"):
            return 2
        elif(canvas[position["y"]][position["x"]-1]!="#" and canvas[position["y"]][position["x"]-1]!="X"):
            return 3
        elif(canvas[position["y"]][position["x"]+1]!="#" and canvas[position["y"]][position["x"]+1]!="X"):
            return 4

def Intcode(code1,debug=0):
    i=0
    while(i<100):
        code1.append(0)
        i+=1
    dim=41
    position={"x":int(dim/2)+1,"y":int(dim/2)+1}
    new_position={"x":int(dim/2)+1,"y":int(dim/2)+1}
    canvas=[[" " for i in range(dim)] for i in range(dim)]
    canvas[position["y"]][position["x"]]="D"
    relative_base=0
    oxygen_position={}
    success_direction=0
    code=list(code1)
    shortest_path=0
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
                    """ render_map(canvas)
                    user_input=input("Ask for input")
                    if(user_input=="w"):
                        user_input=1
                    elif(user_input=="s"):
                        user_input=2
                    elif(user_input=="a"):
                        user_input=3
                    elif(user_input=="d"):
                        user_input=4
                    else:
                        user_input=get_direction(success_direction, position, canvas)
                        print(user_input) """
                    user_input=get_direction(success_direction, position, canvas)

                    if(user_input==1): # north
                        new_position["y"]=position["y"]-1
                        new_position["x"]=position["x"]
                    elif(user_input==2): # south
                        new_position["y"]=position["y"]+1
                        new_position["x"]=position["x"]
                    elif(user_input==3): # west
                        new_position["y"]=position["y"]
                        new_position["x"]=position["x"]-1
                    elif(user_input==4): # east
                        new_position["y"]=position["y"]
                        new_position["x"]=position["x"]+1
                
                    if(C=="2"):
                        code[relative_base+code[i+1]]=user_input
                    else:
                        code[code[i+1]]=user_input
                    i+=2
                else:
                    if(DE=="04"):
                        param1=get_param1(code, i, A,B,C, relative_base)
                        if(param1==0):
                            canvas[new_position["y"]][new_position["x"]]="#"
                        elif(param1==1):
                            if canvas[new_position["y"]][new_position["x"]]==" ":
                                canvas[position["y"]][position["x"]]="."
                                shortest_path+=1
                            else:
                                canvas[position["y"]][position["x"]]="X"
                                shortest_path-=1
                            canvas[new_position["y"]][new_position["x"]]="D"
                            position["y"]=int(new_position["y"])
                            position["x"]=int(new_position["x"])

                        elif(param1==2):
                            canvas[new_position["y"]][new_position["x"]]="O"
                            canvas[position["y"]][position["x"]]="."
                            position["y"]=int(new_position["y"])
                            position["x"]=int(new_position["x"])
                            shortest_path+=1
                            oxygen_position["y"]=int(new_position["y"])
                            oxygen_position["x"]=int(new_position["x"])
                            print("Oxygen position: " + str(oxygen_position))
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
                                                canvas[oxygen_position["y"]][oxygen_position["x"]]="O"
                                                render_map(canvas)
                                                return canvas
                                            else:
                                                print("ERROR")
                                                return [None]

import copy
def spread_oxygen(canvas):
    counter=0
    full=0
    exit_code=0
    while(exit_code!=1):
        updated_canvas=copy.deepcopy(canvas)
        change=0
        i=0
        for row in canvas:
            j=0
            for col in row:
                if(col=="O"):
                    if canvas[i][j-1] == "X":
                        updated_canvas[i][j-1] = "O"
                        change=1
                    if canvas[i][j+1] == "X":
                        updated_canvas[i][j+1] = "O"
                        change=1
                    if canvas[i-1][j] == "X":
                        updated_canvas[i-1][j] = "O"
                        change=1
                    if canvas[i+1][j] == "X":
                        updated_canvas[i+1][j] = "O"
                        change=1
                j+=1
            i+=1
        canvas=copy.deepcopy(updated_canvas)
        counter+=1
        print("Counter: "+ str(counter) + " Minutes: " + str(counter*2))
        render_map(canvas)
        exit_code=input("Exit?")

filename = "Day15/input.txt"
file = open(filename, "r")
input_txt=file.readline()
input_txt=make_int_list(input_txt)

maze_map=Intcode(input_txt,0)

spread_oxygen(maze_map)