tests = int(input(""))
while(tests>0):
    tests -= 1
    books  = int(input(""))
    Sum = 0
    x = float("inf")
    d = {"10":x,"01":x,"11":x}
    while(books>0):
        books-=1
        time,skills = input().split()
        time = int(time)
        if skills!="00":
            d[skills] = min(d.get(skills),time)
    if (((d.get("10")==x) or (d.get("01")==x)) and (d.get("11")==x)):
        print(-1)
    else:
        print(min(d.get("10")+d.get("01"),d.get("11")))
