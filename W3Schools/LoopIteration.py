Ques=str(input("While Loop or For Loop ? : "))
if(Ques=="While"):    
    i=1
    while(i<=3):
        print(i,"Outer loop")
        j=1
        while(j<=3):
            print(j,"Inner loop")
            j=j+1
        i=i+1
        print("----------")
elif(Ques=="For"):
    for i in range(1,4):
        print("Outer loop iteration",i)
        for j in range(1,4):
            print("Inner loop iteration",j)
        print("------------")

