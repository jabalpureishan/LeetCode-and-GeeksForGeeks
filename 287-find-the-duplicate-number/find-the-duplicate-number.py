class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set_ = set()
        for i in nums:
            if i in set_:
                return i
            set_.add(i)