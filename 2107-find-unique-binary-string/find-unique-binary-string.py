class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        lens = len(nums[0])
        if lens==1:
            if nums==["1"]:
                return "0"
            else:
                return "1"

        start = 2**(lens-1)
        end = 2**(lens)+1
        nums = set(nums)
        if "0"*lens not in nums:
            return "0"*lens
        for i in range(start,end):
            curr = bin(i)[2:]
            if curr not in nums:
                return curr

        