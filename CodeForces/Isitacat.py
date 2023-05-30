Test = int(input(""))
while(Test>0):
    Test -= 1
    L = int(input(""))
    I = input("")
    I=I.lower()
    Done =""
    for i in I:
        if i not in Done:
            Done = Done + i
    if(Res=="meow"):
        print("YES")
    else:
        print("NO")

