def Find_average():
    string= input("enter numbers")
    string=string.lower().split()
    total_numbers=len(string)
    Sum=0
    i=0
    while (total_numbers>i):
        Sum= Sum+int(string[i])
        i=i+1
    average = Sum/total_numbers
    print (average)


Find_average()


    
