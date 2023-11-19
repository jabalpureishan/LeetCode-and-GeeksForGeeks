class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        set_ = sorted(set(nums))
        n = {}
        for i in range(len(set_)):
            n[set_[i]] = i
        ans = 0
        for i in nums:
            ans += n[i]
        return ans