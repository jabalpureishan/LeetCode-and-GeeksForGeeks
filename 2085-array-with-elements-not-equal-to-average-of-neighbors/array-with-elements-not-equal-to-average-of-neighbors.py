class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        nums.sort()
        ind = 0
        for i in range(0,n,2):
            ans[i] = nums[ind]
            ind += 1
        for i in range(1,n,2):
            ans[i] = nums[ind]
            ind += 1
        return ans
        