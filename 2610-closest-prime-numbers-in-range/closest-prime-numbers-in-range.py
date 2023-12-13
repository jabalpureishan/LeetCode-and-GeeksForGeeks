class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(N):
                arr = [False]*2+[True]*(N-1)
                root = sqrt(N)
                i = 2
                while i<=root:
                    if arr[i]:
                        for j in range(i*i,N+1,i):
                            arr[j] = False
                    i += 1
                return arr
            
        # if right-left<=2:
        #     return [-1,-1]
        s = sieve(right)
        ans = [-1,-1]
        Min = float("inf")
        prev = 0
        for i in range(left,right+1):
            if s[i]:
                if prev!=0 and i-prev<Min:
                    Min = i-prev
                    ans = [prev,i]
                    if Min in {1,2}:
                        return ans
                prev = i
        return ans
    