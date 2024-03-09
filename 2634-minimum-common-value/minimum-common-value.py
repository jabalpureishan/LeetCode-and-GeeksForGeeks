class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set_ = set(nums2)
        Min = float("inf")
        for i in nums1:
            if i in set_:
                Min = min(Min,i)
        if Min==float("inf"):
            return -1
        return Min
        