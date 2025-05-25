class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        length = len(nums)
        i,j = 0,length-1
        count = 0
        while i<j:
            Sum = nums[i]+nums[j]
            if Sum<k:
                i += 1
            elif Sum>k:
                j -= 1
            else:
                count += 1
                i += 1
                j -= 1
        return count

        