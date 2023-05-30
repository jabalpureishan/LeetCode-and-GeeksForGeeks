n=6
for i in range(1,7):
    print()
    print(n*" ",end="")
    for j in range(1,i+1):
        if((i==3 and j==2) or (i==4 and j==2) or (i==4 and j==3) or (i==5 and j==2) or (i==5 and j==3) or (i==5 and j==4)):
            print("  ",end="")
        else:
            print(" *",end="")
    n=n-1