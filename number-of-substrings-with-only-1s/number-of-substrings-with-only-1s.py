class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        Sum = 0 
        s = s + "$"
        for i in s:
            #print("i:",i)
            if i=="1":
                #print("count increment")
                count += 1
                #print("------------")
            else:
                #print("count:",count)
                #print("sum update:",(count*(count + 1))//2)
                #print("sum before:",Sum)
                Sum += (count*(count + 1))//2
                #print("sum after:",Sum)
                count = 0
                #print("count reset")
                #print("---------")
            #print("************")
        return Sum%(10**9 + 7)