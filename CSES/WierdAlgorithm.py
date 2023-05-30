N = int(input(""))
while(True):
    if(N==1):
        print(1)
        break
    print(N,end=" ")
    if(N%2==0):
        N = N//2
    else:
        N = N*3 + 1