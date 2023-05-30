def mix(C):
    try:
        max(C)
    except:
        return(0)
    else:
        return(max(C))


def mex(B):
    for i in range(0,mix(B)+2):
        if i not in B:
            return(i)

def maximum(A,L):
    result = 0
    for i in range(1,L+1):
        Ans = mex(A[0:i]) + mex(A[i:])
        if(Ans>result):
            result = Ans
    return(result)

def main():
    Test  = int(input(""))
    for i in range(Test):
        L = int(input(""))
        A = list(map(int, input().split()))
        print(maximum(A,L))

main()