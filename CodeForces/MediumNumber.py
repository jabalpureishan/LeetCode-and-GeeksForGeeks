T = int(input(""))
for i in range(0,T):
    A = list(map(int, input().split()))
    Mx= max(A)
    Mn=min(A)
    A.remove(Mx)
    A.remove(Mn)
    print(A[0])