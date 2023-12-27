class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if gcd(i,j)==1:

                    ans.append(str(i)+"/"+str(j))

        return ans
        