class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s)

        def check_if_one(s):
            n = len(s)
            if s[:n-1]==["0"]*(n-1) and s[-1]=="1":
                return False
            return True

        def divide(s):
            n = len(s)
            for i in range(n-2,-1,-1):
                s[i+1] = s[i]
            s[0] = "0"
            return s

        def add(s):
            ind = len(s)-1
            carry = 1
            while carry>0 and ind>-1:
                if s[ind]=="0":
                    s[ind] = "1"
                    carry = 0
                    break
                else:
                    s[ind] = "0"
                    carry = 1

                ind -= 1
            if carry>0:
                s = ["1"] + s
            return s

        count = 0 
        while check_if_one(s):
            count += 1
            if s[-1]=="1":
                s = add(s)
            else:
                s = divide(s)
        return count