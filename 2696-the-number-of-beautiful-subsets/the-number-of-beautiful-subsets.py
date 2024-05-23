class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = len(nums)
        nums.sort()
        for i in range(2,len(nums)+1):
            n = combinations(nums,i)
            for j in n:
                j = set(j)
                for l in j:
                    if l+k in j or l-k in j:
                        break
                else:
                    ans += 1
        return ans