ques=str(input("Execute using For/While ? "))
if(ques=="For"):
    n=6
    for i in range(1,7):
        print()
        print(n*" ",end="")
        for j in range(1,i):
            print(" *", end="")
        n=n-1
else:
    i=1
    n=5
    while(i<=5):
        print()

        print(n*" ",end="")
        j=1
        while(j<=i):
            print(" *",end="")
            j=j+1
        i=i+1
        n=n-1