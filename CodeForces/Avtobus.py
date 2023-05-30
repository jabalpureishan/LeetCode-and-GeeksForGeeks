Test=int(input(""))
for i in range(Test):
    W = int(input(""))
    if((W%2==0) and (W>=4)):
        if(W%6==0):
            print(W//6,end=" ")
        else:
            print((W//6)+1,end=" ")
        print(W//4)
    else:
        print(-1)
    