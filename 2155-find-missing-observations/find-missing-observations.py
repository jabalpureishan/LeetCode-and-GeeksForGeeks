class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        ans = [1]*n
        curr = n
        total = mean*(n+len(rolls))-sum(rolls)
        if total<curr:
            return []
        ind = 0
        while curr<total and ans[-1]!=6:
            #print(ind)
            ans[ind%n] += 1
            ind += 1
            curr += 1
        if curr<total:
            return []
        return ans
        