def solve(Pile,target):
    if Pile==target:
        return "YES"
    if target>Pile:
        return "NO"
    if Pile%3!=0:
        return "NO"
    Max = Pile
    Piles = {Pile}
    while(Max>target):
        if not Piles:
            break
        if Max%3!=0:
            Piles.remove(Max)
            if not Piles=={}:
                break
            Max = max(Piles)
            continue
        Max = max(Piles)       
        v = Max//3
        Piles.add(v)
        Piles.add(2*v)
        Piles.remove(Max)
        Max = max(Piles)
        #print("Max:",Max)
        #print(Piles)
        if target in Piles:
            return "YES"
    return "NO"

tests = int(input(""))
while(tests>0):
    tests -= 1
    Pile,target = map(int, input().split())
    print(solve(Pile,target))
