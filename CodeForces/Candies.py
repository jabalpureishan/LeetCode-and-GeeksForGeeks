Test = int(input(""))
for i in range(Test):
    N = int(input(""))
    for i in range(2,N):
        if((N%((2**i)-1))==0):
            X = N//((2**i)-1)
            break
    print(X)