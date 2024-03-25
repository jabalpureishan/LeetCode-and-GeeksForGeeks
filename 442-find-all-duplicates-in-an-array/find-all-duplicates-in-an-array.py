class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans,set_ = [],set()
        for i in nums:
            if i in set_:
                ans.append(i)
            set_.add(i)
        return ans