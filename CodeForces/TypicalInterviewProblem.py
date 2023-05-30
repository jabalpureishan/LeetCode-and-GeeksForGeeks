Test = int(input(""))
while(Test>0):
    Test -= 1
    Length = int(input(""))
    String = input("")
    i = 1
    Answer = ""
    while(i<152):
        i+=1
        if(i%5==0):
            Answer = Answer + "B"
        if(i%3==0):
            Answer = Answer + "F"
    if String in Answer:
        print("YES")
    else:
        print("NO")