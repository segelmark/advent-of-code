user_input=1
def get_input():
    user_input=int(input("Please make input: "))
    return(user_input)

def output(output):
    # print("Output: " + str(output))
    return output

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


def opcode1(snippet, position, A,B,C):
    if(C=="0"):
        param1=snippet[snippet[position+1]]
    else:
        param1=snippet[position+1]
    if(B=="0"):
        param2=snippet[snippet[position+2]]
    else:
        param2=snippet[position+2]
    snippet[snippet[position+3]]=param1+param2
    position=position+4
    return snippet, position
    
def opcode2(snippet, position, A,B,C):
    if(C=="0"):
        param1=snippet[snippet[position+1]]
    else:
        param1=snippet[position+1]
    if(B=="0"):
        param2=snippet[snippet[position+2]]
    else:
        param2=snippet[position+2]
    snippet[snippet[position+3]]=param1*param2
    position=position+4
    return snippet, position

def opcode4(snippet, position, A,B,C):
    if(C=="0"):
        param1=snippet[snippet[position+1]]
    else:
        param1=snippet[position+1]
    output(param1)
    position=position+2
    return snippet, position, param1

def opcode5(snippet, position, A,B,C):
    if(C=="0"):
        param1=snippet[snippet[position+1]]
    else:
        param1=snippet[position+1]
    if(B=="0"):
        param2=snippet[snippet[position+2]]
    else:
        param2=snippet[position+2]
    if(param1):
        position=param2
    else:
        position=position+3
    return snippet, position

def opcode6(snippet, position, A,B,C):
    if(C=="0"):
        param1=snippet[snippet[position+1]]
    else:
        param1=snippet[position+1]
    if(B=="0"):
        param2=snippet[snippet[position+2]]
    else:
        param2=snippet[position+2]
    if(param1 == 0):
        position=param2
    else:
        position=position+3
    return snippet, position

def opcode7(snippet, position, A,B,C):
    if(C=="0"):
        param1=snippet[snippet[position+1]]
    else:
        param1=snippet[position+1]
    if(B=="0"):
        param2=snippet[snippet[position+2]]
    else:
        param2=snippet[position+2]
    if(param1<param2):
        snippet[snippet[position+3]]=1
    else:
        snippet[snippet[position+3]]=0
    position=position+4
    return snippet, position

def opcode8(snippet, position, A,B,C):
    if(C=="0"):
        param1=snippet[snippet[position+1]]
    else:
        param1=snippet[position+1]
    if(B=="0"):
        param2=snippet[snippet[position+2]]
    else:
        param2=snippet[position+2]
    if(param1==param2):
        snippet[snippet[position+3]]=1
    else:
        snippet[snippet[position+3]]=0
    position=position+4
    return snippet, position

def make_int_list(input_txt):
    string_array=input_txt.split(",")
    return [int(i) for i in string_array]

def Intcode(code1,inputs=[],noun=None,verb=None,debug=0):
    code=list(code1)
    input_counter=0
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
            print(code)
        A, B, C, DE = get_parameters_modes(command)
        if(DE=="01"):
            code, i = opcode1(code,i,A,B,C)
        else:
            if(DE=="02"): 
                code, i = opcode2(code,i,A,B,C)
            else:
                if(DE=="03"): 
                    if(len(inputs)>input_counter):
                        code[code[i+1]]=inputs[input_counter]
                    else:
                        code[code[i+1]]=get_input()
                    input_counter+=1
                    i=i+2
                else:
                    if(DE=="04"): 
                        code, i, output = opcode4(code,i,A,B,C)
                    else:
                        if(DE=="05"): 
                            code, i = opcode5(code,i,A,B,C)
                        else:
                            if(DE=="06"): 
                                code, i = opcode6(code,i,A,B,C)
                            else:
                                if(DE=="07"): 
                                    code, i = opcode7(code,i,A,B,C)
                                else:
                                    if(DE=="08"): 
                                        code, i = opcode8(code,i,A,B,C)
                                    else:
                                        if(DE=="99"):
                                            return output
                                        else:
                                            print("ERROR")
                                            return [None]

def amp_controller(phase_sequence,computer):
    signal=0
    for phase in phase_sequence:
        signal=Intcode(computer,[phase,signal],None,None,0)
    return signal

#Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0):
print(amp_controller([4,3,2,1,0],[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]))

#Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4):
print(amp_controller([0,1,2,3,4],[3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]))

#Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2):
print(amp_controller([1,0,4,3,2],[3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]))

filename = "Day7/input.txt"
file = open(filename, "r")
input_txt=file.readline()
input_txt=make_int_list(input_txt)
i=0
max=0
while(i<=4):
    j=0
    while(j<=4):
        if(j!=i):
            k=0
            while(k<=4):
                if(k!=i and k!=j):
                    l=0
                    while(l<=4):
                        if(l!=i and l!=j and l!=k):
                            m=0
                            while(m<4):
                                if(m!=i and m!=j and m!=k and m!=l):
                                    new=amp_controller([i,j,k,l,m],input_txt)
                                    if(new>max):
                                        max=new
                                m+=1
                        l+=1
                k+=1
        j+=1
    i+=1
print(max)