class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        Mod = pow(10,9) + 7
        d,ans = {},0
        for i in nums:
            curr = i-int(str(i)[::-1])
            d[curr] = d.get(curr,0) + 1
        for i in d:
            ans += (((d[i]-1)*d[i])//2)%Mod
        return ans%Mod


        