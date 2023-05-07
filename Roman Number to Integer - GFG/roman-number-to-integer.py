#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        s = S
        D = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"CM":900,"IV":4,"XC":90}
        length = len(s)
        output = D.get(s[0])
        for i in range(1,length):
            current = D.get(s[i])
            prev = D.get(s[i-1])
            if current>prev :
                output += current - 2*prev
            else:
                output += current
        return output



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends