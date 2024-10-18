class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime,ans = [False,False]+[True]*n,[]
        i = 2
        while i*i<=n:
            if prime[i]:
                for j in range(i*i,n+1,i):
                    prime[j] = False
            i += 1
        for ind,val in enumerate(prime):
            if val==True and ind<=n: ans.append(ind)
        left,right = 0,len(ans)-1
        res = []
        while left<=right:
            #print(ans[left]+ans[right])
            if ans[left]+ans[right]<n:
                left += 1
            elif ans[left]+ans[right]>n:
                right -= 1
            else:
                res.append([ans[left],ans[right]])	
                left += 1
                right -= 1
        return res
            