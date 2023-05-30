N = int(input(""))
A = list(map(int, input().split()))
count = 0
for i in range(1,N):
    if(A[i]<A[i-1]):
        Diff =  A[i-1] - A[i] 
        count = count + Diff
        A[i] = A[i] + Diff
print(count)