class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        Output = nums1[:m]
        nums1.clear()
        for i in range(m):
                nums1.append(Output[i])
        for i in range(n):
                nums1.append(nums2[i])
        nums1.sort()

  