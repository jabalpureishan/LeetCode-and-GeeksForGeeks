N=int(input("Enter Number : "))
for i in range(1,N+1):
    if(N%i==0):
        print(i,end=",")