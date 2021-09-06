import time

def make_pattern(base_pattern, input_list, digit_pos):
    pattern=[]
    j=0
    while len(pattern)<=len(input_list):
        for number in base_pattern:
            i=0
            while i<digit_pos:
                pattern.append(number)
                i+=1
        j+=1
    pattern.pop(0)
    return pattern

def make_patterns(base_pattern, input_list):
    patterns=[]
    i=0
    while len(patterns)<len(input_list):
        patterns.append(make_pattern(base_pattern, input_list, i+1))
        i+=1
    return patterns

def FFT_phase(input_list, patterns):
    digit_pos=1
    output=""
    for number in input_list:
        output+=str(FFT_element(input_list, patterns, digit_pos))
        digit_pos+=1
    return output


def FFT_element(input_list, patterns, digit_pos):
    element=0
    i=0
    pattern=patterns[digit_pos-1]
    for number in input_list:
        element+=int(number)*pattern[i%len(pattern)]
        i+=1
    element=str(element)
    return element[-1:]

def FFT(input_list, base_pattern, phases):
    output=input_list
    patterns=make_patterns(base_pattern, input_list)
    phase=0
    while(phase<phases):
        output=FFT_phase(output, patterns)
        phase+=1
    return output

base_pattern=[0, 1, 0, -1]

""" input_list="12345678"

print(make_pattern(base_pattern, input_list, 1))
print(make_patterns(base_pattern, input_list))

print(FFT("12345678", base_pattern, 1)) """

"""if FFT("12345678", base_pattern, 4)!="01029498":
    print("Error!")

start_time = time.time()

print("80871224585914546619083218645595 becomes 24176176:")
input_list="80871224585914546619083218645595"
print(FFT(input_list, base_pattern, 100))

print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()

print("19617804207202209144916044189917 becomes 73745418:")
input_list="19617804207202209144916044189917"
print(FFT(input_list, base_pattern, 100))

print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()

print("69317163492948606335995924319873 becomes 52432133:")
input_list="69317163492948606335995924319873"
print(FFT(input_list, base_pattern, 100))

print("--- %s seconds ---" % (time.time() - start_time))
"""

def fft2(input_list, phases):
    output=input_list
    seven=int(input_list[0:7])
    
    print(seven)
    phase=0
    while(phase<phases):
        new_output=[]
        test=list(input_list[seven:])
        i=1
        sum=0
        while(i<=len(test)):
            sum+=int(output[-i])
            test[-i]=str(sum%10)
            i+=1
        phase+=1
        print(phase)
        output=list(test)
    input_list="".join(output)
    return input_list[0:8]

input_list="03036732577212944063491565474664" # becomes 84462026
long_input=""
#input_list="02935109699940807407585447034323" # becomes 78725270.
#input_list="03081770884921959731165446850517" # becomes 53553731

filename = "Day16/input.txt"
file = open(filename, "r")
input_list=file.readline()
#print(FFT(input_list, base_pattern, 100))


i=0
while(i<10000):
    long_input+=input_list
    i+=1

start_time = time.time()

print(fft2(long_input, 100))

#print(FFT(input_list, base_pattern, 100))

print("--- %s seconds ---" % (time.time() - start_time))

