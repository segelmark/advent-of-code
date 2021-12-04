user_input=1
def get_input():
    user_input=int(input("Please make input: "))
    return(user_input)

def output(output):
    print("Output: " + str(output))

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

def opcode1(snippet, position, A,B,C, relative_base):
    param1, param2, param3 = get_parameter(snippet, position, A,B,C, relative_base)
    
    snippet[param3]=param1+param2
    position=position+4
    return snippet, position
    
def opcode2(snippet, position, A,B,C, relative_base):
    param1, param2, param3 = get_parameter(snippet, position, A,B,C, relative_base)

    snippet[param3]=param1*param2
    position=position+4
    return snippet, position

def opcode3(snippet, position, A,B,C, relative_base):
    if(C=="2"):
        snippet[relative_base+snippet[position+1]]=user_input
    else:
        snippet[snippet[position+1]]=user_input
    position=position+2
    return snippet, position

def opcode4(snippet, position, A,B,C, relative_base):
    if(C=="0"):
        param1=snippet[snippet[position+1]]
    else:
        if(C=="2"):
            param1=snippet[relative_base+snippet[position+1]]
        else:
            param1=snippet[position+1]
    output(param1)
    position=position+2
    return snippet, position

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

def opcode9(snippet, position, A,B,C, relative_base):
    if(C=="0"):
        param1=snippet[snippet[position+1]]
    else:
        if(C=="2"):
            param1=snippet[relative_base+snippet[position+1]]
        else:
            param1=snippet[position+1]

    position=position+2

    relative_base=relative_base+param1

    return snippet, position, relative_base

def make_int_list(input_txt):
    string_array=input_txt.split(",")
    return [int(i) for i in string_array]

def Intcode(code1,noun=None,verb=None,debug=0):
    i=0
    while(i<10000):
        code1.append(0)
        i+=1
    relative_base=0
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
            code, i = opcode1(code,i,A,B,C,relative_base)
        else:
            if(DE=="02"): 
                code, i = opcode2(code,i,A,B,C,relative_base)
            else:
                if(DE=="03"): 
                    code, i = opcode3(code,i,A,B,C,relative_base)
                else:
                    if(DE=="04"): 
                        code, i = opcode4(code,i,A,B,C,relative_base)
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
                                            code, i, relative_base = opcode9(code,i,A,B,C,relative_base)
                                        else:
                                            if(DE=="99"):
                                                return code
                                            else:
                                                print("ERROR")
                                                return [None]


# Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
user_input=1
print("Should output 1")
Intcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
Intcode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1])

user_input=0
print("Should output 0")
Intcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
Intcode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1])

# Will output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8
user_input=7
print("Should output 999")
Intcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
user_input=8
print("Should output 1000")
Intcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
user_input=9
print("Should output 1001")
Intcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])

# Using position mode, output 1 (if it is) or 0 (if it is not)
user_input=7
print("Should output 1")
Intcode([3,9,7,9,10,9,4,9,99,-1,8]) # Consider whether the input is LESS THAN 8
print("Should output 0")
Intcode([3,9,8,9,10,9,4,9,99,-1,8]) # Consider whether the input is EQUAL TO 
user_input=8
print("Should output 0")
Intcode([3,9,7,9,10,9,4,9,99,-1,8]) # Consider whether the input is LESS THAN 8
print("Should output 1")
Intcode([3,9,8,9,10,9,4,9,99,-1,8]) # Consider whether the input is EQUAL TO 8

# Using immediate mode, consider whether the input is LESS THAN 8; output 1 (if it is) or 0 (if it is not).
#print(Intcode([3,3,1107,-1,8,3,4,3,99]))

# Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
#print(Intcode([3,3,1108,-1,8,3,4,3,99]))


Intcode([1002,4,3,4,33])
Intcode([1101,100,-1,4,0])
Intcode([1,0,0,0,99])
print("Should output " + str(user_input))
Intcode([3,0,4,0,99])

error=0

# 104,1125899906842624,99 should output the large number in the middle.
Intcode([104,1125899906842624,99])
# 1102,34915192,34915192,7,4,7,99,0 should output a 16-digit number.
Intcode([1102,34915192,34915192,7,4,7,99,0])
# 109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99 takes no input and produces a copy of itself as output.
#Intcode([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])

Intcode([109,48,1201,0,0,44,1001,3,2,3,1201,1,0,19,1001,11,2,11,104,0,1001,43,1,43,8,43,44,45,1006,45,18,1101,0,0,43,8,3,47,40,1106,0,2,99,0,0,0,0,784,7,32,1,46,5,32,1,46,23,32,3,42,1,32,2,42,1,10,16,32,1,33,6,32,1,46,11,32,1,46,1,95,1,42,1,46,23,32,1,46,1,10,13,32,1,45,1,32,1,45,1,42,1,45,1,32,1,45,7,32,1,46,1,45,1,39,1,45,1,46,3,32,1,33,2,32,1,33,5,32,1,46,1,10,4,32,1,46,4,32,1,46,6,32,1,42,7,32,1,46,1,45,1,39,1,32,1,46,1,45,1,46,1,32,1,39,1,45,1,46,1,33,2,32,1,33,13,32,1,46,14,32,1,46,1,10,15,32,3,42,3,32,1,46,1,45,1,39,1,32,1,46,1,45,1,39,3,32,1,39,1,45,1,46,1,32,1,39,1,45,1,46,1,33,4,32,1,46,1,10,7,32,1,42,7,32,3,42,1,46,1,45,1,39,1,32,1,46,1,45,1,39,9,32,1,39,1,45,1,46,1,32,1,39,1,45,1,46,19,32,1,46,1,10,7,32,1,42,6,32,3,42,1,36,1,42,1,46,1,45,1,39,15,32,1,39,1,45,1,46,1,32,1,39,1,45,1,46,5,32,1,42,1,10,2,32,1,42,3,32,3,42,5,32,1,42,1,32,3,42,5,32,11,95,5,32,1,33,1,45,2,46,1,33,1,45,1,46,2,32,1,42,5,32,1,42,9,32,1,42,4,32,1,42,1,10,2,32,1,42,3,32,3,42,4,32,2,42,1,36,2,42,1,32,1,42,3,32,1,33,2,95,1,33,2,95,1,33,2,95,1,33,2,95,1,33,4,32,1,33,4,32,1,33,2,32,3,42,3,32,3,42,4,32,1,46,3,32,1,42,3,32,3,42,1,10,1,32,3,42,1,32,4,42,4,32,1,42,1,32,5,42,3,32,1,33,2,95,1,33,2,95,1,33,2,95,1,33,2,95,1,33,4,32,1,33,6,32,1,46,3,42,1,45,1,46,1,45,3,42,1,32,1,42,5,32,3,42,1,32,1,42,1,32,1,35,1,95,1,10,10,42,2,32,1,42,1,32,4,42,1,36,1,32,1,42,2,32,1,33,2,95,1,33,2,95,1,33,2,95,1,33,2,95,1,33,4,32,1,33,1,45,2,46,2,45,1,39,5,42,3,32,1,35,1,32,1,39,1,42,1,45,2,46,3,45,1,35,1,32,3,42,1,10,4,42,1,32,5,42,2,32,1,42,1,32,1,36,2,42,1,32,3,42,6,32,1,46,12,32,1,33,6,32,5,42,5,32,3,42,7,32,3,42,1,10,12,42,1,32,5,42,1,32,3,42,1,45,2,46,1,45,1,39,1,32,1,45,2,46,9,95,1,33,5,32,7,42,4,32,3,42,6,32,5,42,1,10,11,42,3,32,1,46,1,45,1,35,1,46,1,45,1,39,11,32,1,39,1,45,1,46,1,45,2,39,1,45,2,46,1,33,5,32,7,42,3,32,4,42,3,46,5,32,1,35,1,10,2,32,1,35,1,32,2,39,1,45,1,46,3,45,2,39,27,32,1,39,1,45,4,46,3,45,1,35,2,46,2,45,1,39,6,42,1,32,2,39,1,45,1,46,3,45,2,39,1,45,1,10,18,32,1,77,1,101,2,114,1,121,1,32,1,67,1,104,1,114,1,105,1,115,1,116,1,109,1,97,1,115,1,10,18,32,1,126,1,82,1,117,1,100,1,111,1,108,1,112,1,104,1,80,1,108,1,97,1,121,1,115,1,126,1,10])

user_input=2
filename = "Day9/input.txt"
file = open(filename, "r")
input_txt=file.readline()
input_txt=make_int_list(input_txt)
Intcode(input_txt,None,None,0)