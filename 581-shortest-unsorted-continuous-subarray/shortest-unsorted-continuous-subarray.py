class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        srted = sorted(nums)
        length = len(nums)
        Min = length
        arr = []
        count = 0
        for i in range(length):
            if srted[i]!=nums[i]:
                arr.append(i)
        if len(arr)==0:
            return 0
        return arr[-1]-arr[0]+1
        