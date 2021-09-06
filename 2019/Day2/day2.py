def opcode1(snippet, position):
    snippet[snippet[position+3]]=snippet[snippet[position+1]]+snippet[snippet[position+2]]
    return snippet
def opcode2(snippet, position):
    snippet[snippet[position+3]]=snippet[snippet[position+1]]*snippet[snippet[position+2]]
    return snippet

def make_int_tuple(input):
    string_array=input.split(",")
    return tuple([int(i) for i in string_array])

def Intcode(code1,noun,verb):
    code=list(code1)
    code[1]=noun
    code[2]=verb
    i=0
    while(i<len(code)):
        command=code[i]
        if(command==1):
            code=opcode1(code,i)
        else:
            if(command==2): 
                code=opcode2(code,i)
            else:
                if(command==99):
                    return code
                else:
                    print("ERROR")
                    return [None]
        i+=4

""" filename = "Day2/input.txt"
file = open(filename, "r")
input=(file.readline()) """


error=0
if(Intcode([1,0,0,0,99],0,0)!=[2, 0, 0, 0, 99]):
    error=1
if(Intcode([2,3,0,3,99],3,0)!=[2,3,0,6,99]):
    error=1
if(Intcode([2,4,4,5,99,0],4,4)!=[2,4,4,5,99,9801]):
    error=1
if(Intcode([1,1,1,4,99,5,6,0,99],1,1)!=[30,1,1,4,2,5,6,0,99]):
    error=1
if(Intcode([1,9,10,3,2,3,11,0,99,30,40,50],9,10)!=[3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]):
    error=1
if(error):    
    print("ERROR")
else:
    print("TEST OK")

filename = "Day2/input.txt"
file = open(filename, "r")
input=file.readline()
input=make_int_tuple(input)


n=0
while(n<=99):
    v=0
    while(v<=99):
        output=Intcode(input,n,v)
        if(output[0]==19690720):
            print(n)
            print(v)
            print(n*100+v)
        v+=1
    n+=1
