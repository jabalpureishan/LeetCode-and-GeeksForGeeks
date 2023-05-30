N = int(input(""))
M = N - 1
A = tuple(map(int, input().split()))
Sum,Max = 0,A[0]
for i in range(M):
    if(A[i]>Max):
        Max = A[i]
    Sum += A[i]
if(Max<N):
    print(N)
else:
    Total = (Max*(Max+1))//2
    print(Total - Sum) 
