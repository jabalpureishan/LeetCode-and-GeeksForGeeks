
T = int(input(""))
for i in range(T):
    length = int(input(""))
    A = list(map(int, input().split()))
    flag = True
    def counta(i):
        count = 0
        for j in A:
            if(j==i):
                count = count + 1
        return(count)
    for i in A:
        if(counta(i)>1):
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")



