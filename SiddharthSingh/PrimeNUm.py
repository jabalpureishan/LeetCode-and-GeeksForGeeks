x,y=input("Print Prime Numbers from : ").split()
x,y=int(x),int(y)
for num in range(x,y+1):
    for i in range(2,num):
        if((num%i)==0):
            break
    else:
        print(num,end=",")