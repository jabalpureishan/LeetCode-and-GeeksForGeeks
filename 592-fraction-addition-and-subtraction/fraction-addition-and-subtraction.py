class Solution:
    def fractionAddition(self, expression: str) -> str:
        exp = expression+"+"
        lastNum = None
        lastExp = [None,0]
        for j,i in enumerate(exp):
            if i in {"+","-"} and j!=0:
                if lastNum==None:
                    print("here",j,exp[lastExp[1]:j])
                    lastNum = exp[lastExp[1]:j].split("/")
                    print(lastNum)
                    lastNum = [int(lastNum[0]),int(lastNum[1])]
                else:
                    curr = exp[lastExp[1]+1:j].split("/")
                    num1 = lastNum[0]
                    num2 = int(curr[0])
                    den1 = lastNum[1]
                    den2 = int(curr[1])
                    lcm = den1*den2//gcd(den1,den2)
                    if lastExp[0]=="+":
                        lastNum = [num1*(lcm//den1)+num2*(lcm//den2),lcm]
                    else:
                        lastNum = [num1*(lcm//den1)-num2*(lcm//den2),lcm]
                if lastNum[0]==0:
                    lastNum = [0,1]
                Gcd = gcd(lastNum[0],lastNum[1])
                lastNum[0],lastNum[1] = lastNum[0]//Gcd,lastNum[1]//Gcd

                lastExp = [i,j]
        return str(lastNum[0])+"/"+str(lastNum[1])