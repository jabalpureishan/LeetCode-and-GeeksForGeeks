class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime,ans = [False,False]+[True]*(n-1),[]
        i = 2
        while i*i<=n:
            if prime[i]:
                for j in range(i*i,n+1,i):
                    prime[j] = False
            i += 1
        l,r = 0,n
        res = []
        while l<=r:
            #print(ans[left]+ans[right])
            if l+r<n:
                l += 1
            elif l+r>n:
                r -= 1
            else:
                if prime[l] and prime[r]:
                    res.append([l,r])	
                l += 1
                r -= 1
        return res
            