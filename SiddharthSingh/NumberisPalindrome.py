N=str(input("Enter Number : "))
n=N
a=len(n)
n,N=int(n),int(N)
b=0
while(n>0):
    q=n%10
    n=n//10
    b=b+q*(10**(a-1))
    a=a-1
if(b==N):
    print("Palindrome")
else:
    print("Not a Palindrome")
