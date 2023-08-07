#User function Template for python3
from math import gcd
class Solution:
    def countFractions(self, n, numerator, denominator):
        d, count = {} , 0
        for i in range(n):
            div = gcd(numerator[i],denominator[i])
            base = denominator[i]//div
            if base in d:
                d[base].append(numerator[i]//div)
            else:
                d[base] = [numerator[i]//div]
        #print(d)
        for i in d:
            freq = {}
            for j in d[i]:
                    count += freq.get(j,0)
                    freq[i-j] = freq.get(i-j,0) + 1
        return count


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    numerator = list(map(int,input().split()))
    denominator = list(map(int,input().split()))
    ob = Solution()
    print(ob.countFractions(n,numerator,denominator))
# } Driver Code Ends