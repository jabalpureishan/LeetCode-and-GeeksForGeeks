Test = int(input(""))
for i in range(Test):
    N = int(input(""))
    Res = N//2020
    Ans = N%2020
    if(Ans<=Res):
        print("YES")
    else:
        print("NO")