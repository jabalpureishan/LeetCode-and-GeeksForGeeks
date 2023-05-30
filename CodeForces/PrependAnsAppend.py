T = int(input(""))
for i in range(T):
    L = int(input(""))
    A = input("")
    count = 0
    if(L%2==0):
        N = L/2
    else:
        N = (L+1)/2
    for i in range(int(N)):
        if(A[i]=="0"):
            if(A[(L-1)-i]=="0"):
                break
            if(A[(L-1)-i]=="1"):
                count += 1
        elif(A[i]=="1"):
            if(A[(L-1)-i]=="1"):
                break
            if(A[(L-1)-i]=="0"):
                count += 1
    count=count*2
    print(L-count)