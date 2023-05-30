num1 = input("Enter Number : ")
num = 2
num1 = int(num1)
while (num1>num):
    if((num%2==0) or (num%3==0) or (num%5==0) or (num%7==0)):
        print(end="")
        num = num + 1
    else:
        print(num)
        num = num + 1