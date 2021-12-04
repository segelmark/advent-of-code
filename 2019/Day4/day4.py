def count_possible_passwords(range_start, range_end):
    i=int(range_start)
    count=0
    while(i<=range_end):
        numbers=[int(j) for j in str(i)]
        if(numbers==sorted(numbers)):
            k=1
            double_number=0
            while(k<len(numbers)):
                if(numbers[k]==numbers[k-1]):
                    double_number=1
                    if(k>=2):
                        if(numbers[k]==numbers[k-2]):
                            double_number=0
                    if(k<len(numbers)-1):
                        if(numbers[k]==numbers[k+1]):
                            double_number=0
                    if(double_number):
                        break
                k+=1
            if(double_number):
                count+=1
        i+=1

    print(count)

range_start=111122
range_end=111123
count_possible_passwords(range_start, range_end)

range_start=146810
range_end=612564
count_possible_passwords(range_start, range_end)

