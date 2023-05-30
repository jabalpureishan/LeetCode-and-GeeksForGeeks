tests = int(input(""))
while(tests>0):
    tests -= 1
    length = int(input(""))
    Array = list(map(int, input().split()))
    Array.append(1)
    Max = 0
    count = 0
    for i in Array:
        if i==0:
            count += 1
        else:
            Max = max(Max,count)
            count = 0
    print(Max)