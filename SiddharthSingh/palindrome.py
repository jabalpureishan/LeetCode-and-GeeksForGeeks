N=str(input("Enter Number : "))
Length=len(N)
flag = False
if(Length%2==0):
    T=(Length-1)//2
    for i in range(1,T+1):
        p=i-1
        q=-(p+1)
        if(str[p]==str[q]):
            flag = True
else:
    T=(Length)//2
    for i in range(1,T+1):
        p=i-1
        q=-(p+1)
        if(str[p]==str[q]):
            flag = True
if flag:
    print("Palindrome")
else:
    print("Not a Palindrome")



