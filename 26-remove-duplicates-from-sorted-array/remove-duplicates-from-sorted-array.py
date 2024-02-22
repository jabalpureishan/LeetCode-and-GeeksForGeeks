class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 0
        set_ = set()
        for i in nums:
            if i not in set_:
                set_.add(i)
                nums[ind] = i
                ind += 1
        return ind
        