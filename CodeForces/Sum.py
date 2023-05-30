T = int(input(""))
for i in range(T):
    X= list(map(int, input().split()))
    if( (X[0]+X[1]==X[2]) or (X[1]+X[2]==X[0]) or (X[2]+X[0]==X[1]) ):
        print("YES")
    else:
        print("NO")
