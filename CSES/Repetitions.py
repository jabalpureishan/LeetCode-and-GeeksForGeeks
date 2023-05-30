def length(Inp):
    L = 0
    for i in Inp:
        L += 1
    return(L)

def driver():
    Inp = input("")
    L = length(Inp)
    count = 1
    Max = 1
    for i in range(L-1):
        if(Inp[i]==Inp[i+1]):
            count += 1
        else:
            count = 1
        if(count>Max):
            Max = count
    return(Max)
print(driver())

