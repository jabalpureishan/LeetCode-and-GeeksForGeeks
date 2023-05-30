
def Factors(Input, List):
    if Input < 4:
        return Input
    for i in range(2, int(2+Input//2)):
        if i == (1 + Input // 2):
            List.append(Input)
            Input = 1
            return
        if Input % i == 0:
            List.append(i)
            Input = Input // i
            Factors(Input, List)
            break
    return List

def Combination(List,Input):
    for i in List:
        for j in List:
            if((((i**j)*j)+((j**i)*i))==Input):
                return(i," ",j)           
    else:
        return(1)

def driver():
    Test = int(input(""))
    for i in range(Test):
        List = []
        Input = int(input(""))
        Factors(Input,List)
        P = Combination(List,Input)
        if(len(str(P))>1):
            for i in P:
                print(i,end="")
            print("\n")
        else:
            print(-P)

driver()