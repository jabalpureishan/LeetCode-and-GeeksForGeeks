n=str(input("Enter Word: "))
length=len(n)
A=""
while(length>0):
    A=A+n[length-1]
    length=length-1
if(A==n):
    print("Palindrome")
else:
    print("Not a Palindrome")
