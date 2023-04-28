class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        n = str(bin(n))
        #print(n)
        if n[2]!="1":
            return False
        n = n[3:]
        #print(n)
        z = n.count("0")
        o = n.count("1")
        #print("z:",z,"o",o)
        if z%2==0 :
            if o==0:
                return True
        return False