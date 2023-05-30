
def counter(f):
    count = 0
    for i in range(len(f)-1):
        if(f[i]==f[i+1]):
            count += 1
    return(count)

def main():
    Test = int(input(""))
    for i in range(Test):
        LA,LB = map(int, input().split())
        A = input("")
        B = input("")
        M = counter(A)
        N = counter(B)
        if((M>1) or (N>1) or ((M==1) and (N==1))):
            print("NO")
        elif(((M==1) or (N==1)) and (A[-1]==B[-1])):
            print("NO")
        else:
            print("YES")



main()