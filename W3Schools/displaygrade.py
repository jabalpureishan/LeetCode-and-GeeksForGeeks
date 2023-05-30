Num=int(input("No. of Inputs : "))
while(Num>0):
    Num=Num-1
    Marks=int(input("Enter Marks : "))
    if(Marks<=100 and Marks>90):
        print("S")
    elif(Marks<=90 and Marks>80):
        print("A")
    elif(Marks<=80 and Marks>70):
        print("B")
    elif(Marks<=70 and Marks>60):
        print("C")
    elif(Marks<=60 and Marks>50):
        print("D")
    elif(Marks==50):
        print("E")
    elif(Marks<50 and Marks>=0):
        print("U")
    else:
        print("Enter a valid Score Between 0 and 100")  