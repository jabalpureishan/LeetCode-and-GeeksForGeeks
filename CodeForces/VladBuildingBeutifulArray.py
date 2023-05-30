def solve(Array):
    evencount,oddcount,mineven,minodd = 0,0,float("inf"),float("inf")
    for i in Array:
        if i%2==0:
            evencount += 1
            mineven = min(mineven,i)
        else:
            oddcount += 1
            minodd = min(minodd,i)
    if oddcount==0 or evencount==0:
        return "YES"
    if mineven<minodd:
        return "NO"
    return "YES"

tests = int(input(""))
for i in range(tests):
    length = int(input(""))
    Array = list(map(int, input().split()))
    print(solve(Array))




