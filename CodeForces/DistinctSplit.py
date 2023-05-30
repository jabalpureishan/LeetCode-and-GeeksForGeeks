def distinct(S):
    Res = "".join(set(S))
    return(len(Res))

def cut(L,A):
    count = 0
    for i in range(1,L):
        if(A[i] not in A[0:i]):
            count += 1
        else:
            break
    count += 1
    X = distinct(A[0:count])
    Y = distinct(A[count:])
    return(X+Y)

def main():
    T = int(input(""))
    for i in range(T):
        L = int(input(""))
        A = input("")
        print(cut(L,A))

main()