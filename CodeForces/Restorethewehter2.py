tests = int(input(""))
while(tests>0):
    tests -= 1
    length,k = map(int, input("").split())
    temp = list(map(int, input("").split()))
    real = list(map(int, input("").split()))
    d = {}
    for i in real:
        d[i] = d.get(i,0) + 1
    for i in temp:
        for j in d:
            if d.get(j)!=0:
                if((abs(i-j))<=k):
                    print(j,end=" ")
                    d[j] -= 1
    print()

