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

def opcode3(snippet, position, A,B,C):
    snippet[snippet[position+1]]=user_input
    position=position+2
    return snippet, position

def opcode4(snippet, position, A,B,C):
    if(C=="0"):
        param1=snippet[snippet[position+1]]
    else:
        param1=snippet[position+1]
    output(param1)
    position=position+2
    return snippet, position

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

def Intcode(code1,noun=None,verb=None,debug=0):
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
            print(code)
        A, B, C, DE = get_parameters_modes(command)
        if(DE=="01"):
            code, i = opcode1(code,i,A,B,C)
        else:
            if(DE=="02"): 
                code, i = opcode2(code,i,A,B,C)
            else:
                if(DE=="03"): 
                    code, i = opcode3(code,i,A,B,C)
                else:
                    if(DE=="04"): 
                        code, i = opcode4(code,i,A,B,C)
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
if(Intcode([1,0,0,0,99])!=[2, 0, 0, 0, 99]):
    error=1
if(Intcode([2,3,0,3,99])!=[2,3,0,6,99]):
    error=1
if(Intcode([2,4,4,5,99,0])!=[2,4,4,5,99,9801]):
    error=1
if(Intcode([1,1,1,4,99,5,6,0,99])!=[30,1,1,4,2,5,6,0,99]):
    error=1
if(Intcode([1,9,10,3,2,3,11,0,99,30,40,50])!=[3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]):
    error=1
if(error):    
    print("ERROR")
else:
    print("TEST OK")

user_input=5
filename = "Day5/input.txt"
file = open(filename, "r")
input_txt=file.readline()
input_txt=make_int_list(input_txt)
Intcode(input_txt)