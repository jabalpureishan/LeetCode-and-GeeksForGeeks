ques=str(input("Execute using For/While ? "))
if(ques=="For"):
    num=6
    for i in range(1,6):
        print()
        for j in range(1,num):
            print("*",end="")
        num = num -1
else:
    i=5
    while(i>=1):
        print()
        j=1
        while(i>=j):
            print("*",end="")
            j=j+1
        i=i-1
