class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        set_ = set(range(1,k+1))
        ans = set()
        count = 0
        ind = -1
        while ans!=set_:
            count += 1
            if nums[ind] in range(1,k+1):
                ans.add(nums[ind])
            ind += -1
            
        return count
        