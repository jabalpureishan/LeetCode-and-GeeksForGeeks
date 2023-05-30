n=str(input("Enter string : "))
i=str(input("Enter letter : "))
n=n.replace(""," ")
n=n.split()
print(n)
count = 0
for i in n:
    count=count+1
print("The letter appears",count,"times in the string")