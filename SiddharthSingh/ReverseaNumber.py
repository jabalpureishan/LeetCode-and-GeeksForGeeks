n=int(input("Enter Number : "))
a=0
while(n>0):
    q=n%10
    n=n//10
    print(q,end="")
    a=q+a
print("\nSum of Digits of reversed number : ",a)

flag=False
N=int(input("Enter Number :"))
for i in range(1,N):
    if(N%i==0):
        flag = True
if flag:
    print("Not Prime")
else:
    print("Prime")