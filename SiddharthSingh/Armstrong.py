N=str(input("Enter Number : "))
length=len(N)
n=N 
n,N=int(n),int(N)
a=0
while(n>0):
    q=n%10
    n=n//10
    a=a+ q**length
if(a==N):
    print("Armstrong")
else:
    print("Not Armstrong")