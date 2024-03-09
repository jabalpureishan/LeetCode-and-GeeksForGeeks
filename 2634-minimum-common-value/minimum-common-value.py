class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1,nums2 = set(nums1),set(nums2)
        nums1 = nums1.intersection(nums2)
        if len(nums1)>0:
            return min(nums1)
        return -1
        