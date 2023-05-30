
from itertools import combinations_with_replacement
import math
T = int(input(""))
for i in range(T):
    O = []
    length = int(input(""))
    B = list(map(str, input().split()))
    P = combinations_with_replacement(B,2)
    A = "".join(B)
    for i in P:
        M = math.gcd(int(i[0]),int(i[1]))
        if(M==1):
            X = A.rindex(i[0])
            Y = A.rindex(i[1])
            O.append(int(X)+int(Y)+2)
    if(len(O)==0):
        print(-1)
    else:
        print(max(O))
