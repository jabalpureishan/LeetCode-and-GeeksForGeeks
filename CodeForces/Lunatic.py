def check(Arr):
    return Arr == Arr[::-1]

def f(Arr, x):
    return [every % x for every in Arr]

def b(Arr):
    if all(every == 0 for every in Arr):
        return 0
    for x in range(max(Arr), 0, -1):
        if check(f(Arr, x)):
            return x
    return 1

tests = int(input(""))
while(tests>0):
    tests -= 1
    length = int(input(""))
    Arr = tuple(map(int, input("").split()))
    print(b(Arr))