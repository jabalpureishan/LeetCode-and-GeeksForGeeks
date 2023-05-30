string = "codeforces"
tests = int(input(""))
while(tests>0):
    tests -= 1
    I = input("")
    count = 0
    for i in range(10):
        if I[i]!=string[i] :
            count += 1
    print(count)