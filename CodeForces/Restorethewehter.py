from collections import defaultdict
from traceback import print_exc
tests = int(input(""))
while(tests>0):
    tests -= 1
    length,k = map(int, input("").split())
    temp = list(map(int, input("").split()))
    real = list(map(int, input("").split()))
    newtemp = temp[:]
    newtemp.sort()
    real.sort()
    d = defaultdict(list)
    for i in range(length):
        d[newtemp[i]].append(real[i])
    for i in temp:
        print(d[i].pop(0),end=" ")
    print()
print("jsjjn")print("")