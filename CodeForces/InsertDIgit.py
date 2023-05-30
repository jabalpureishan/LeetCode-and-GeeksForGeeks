test = int(input(""))
while(test>0):
    test -= 1
    length,number = map(int, input().split())
    S = int(input(""))
    A = list(map(int, str(S)))
    flag = True
    for i in range(length):
        print
        if A[i]<number :
            Ans = i
            flag = False
            break
    if flag:
        A.append(number)
    else:
        A.insert(Ans,number)
    O = ""
    for i in A:
        O = O + str(i)
    print(O)
    