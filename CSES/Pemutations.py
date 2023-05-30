I = int(input(""))
if(1<I<4):
    print("NO SOLUTION")
else:
    for i in range(2,I+1,2):
        print(i,end=" ")
    for i in range(1,I+1,2):
        print(i,end=" ")
    
