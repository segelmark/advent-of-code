def render_map(map):
    for row in map:
        string=""
        for col in row:
            if(col==0):
                string+="."
            else:
                string+="#"
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

def Intcode(code1,noun=None,verb=None,debug=0):
    i=0
    while(i<1000):
        code1.append(0)
        i+=1
    dim=132
    tiles_painted={}
    canvas=[[0 for i in range(dim)] for i in range(dim-30)]
    rob_pos={"x":dim//2-30, "y":dim//2}
    canvas[rob_pos["y"]][rob_pos["x"]]=1
    robot_direction=0
    relative_base=0
    output_mode=0
    code=list(code1)
    if(noun!=None):
        code[1]=noun
    if(verb!=None):
        code[2]=verb
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
                    user_input=canvas[rob_pos["y"]][rob_pos["x"]]
                    if(C=="2"):
                        code[relative_base+code[i+1]]=user_input
                    else:
                        code[code[i+1]]=user_input
                    i+=2
                else:
                    if(DE=="04"): 
                        param1=get_param1(code, i, A,B,C, relative_base)
                        if(output_mode==0):
                            tiles_painted[str(rob_pos)]=1
                            canvas[rob_pos["y"]][rob_pos["x"]]=param1
                            output_mode=1
                        else:
                            if(output_mode==1):
                                if(param1==0):
                                    robot_direction=(robot_direction-1)%4
                                else:
                                    robot_direction=(robot_direction+1)%4
                                if(robot_direction==0):
                                    rob_pos={"x":rob_pos["x"], "y":rob_pos["y"]-1}
                                if(robot_direction==1):
                                    rob_pos={"x":rob_pos["x"]+1, "y":rob_pos["y"]}
                                if(robot_direction==2):
                                    rob_pos={"x":rob_pos["x"], "y":rob_pos["y"]+1}
                                if(robot_direction==3):
                                    rob_pos={"x":rob_pos["x"]-1, "y":rob_pos["y"]}
                                output_mode=0
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
                                                print(len(tiles_painted))
                                                render_map(canvas)
                                                return code
                                            else:
                                                print("ERROR")
                                                return [None]


""" # 104,1125899906842624,99 should output the large number in the middle.
Intcode([104,1125899906842624,99])
# 1102,34915192,34915192,7,4,7,99,0 should output a 16-digit number.
Intcode([1102,34915192,34915192,7,4,7,99,0]) 
# 109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99 takes no input and produces a copy of itself as output.
Intcode([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])

print("Should output 0")
Intcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
Intcode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1])

print("Should output 1")
Intcode([3,9,7,9,10,9,4,9,99,-1,8]) # Consider whether the input is LESS THAN 8
print("Should output 0")
Intcode([3,9,8,9,10,9,4,9,99,-1,8]) # Consider whether the input is EQUAL TO 

print("Should output 0")
Intcode([3,0,4,0,99]) """

filename = "Day11/input.txt"
file = open(filename, "r")
input_txt=file.readline()
input_txt=make_int_list(input_txt)
Intcode(input_txt,None,None,0)