test = int(input(""))
for i in range(test):
    L = int(input(""))
    A = input("")
    R = [0,0]
    Ans = [1,1]
    flag = False
    for i in A:
        if(R==Ans):
            flag = True
            break
        else:
            if(i=="U"):
                R[1] += 1
            elif(i=="R"):
                R[0] += 1
            elif(i=="D"):
                R[1] -= 1
            elif(i=="L"):
                R[0] -= 1
    if(R==Ans):
        flag = True
    if flag:
        print("YES")
    else:
        print("NO")