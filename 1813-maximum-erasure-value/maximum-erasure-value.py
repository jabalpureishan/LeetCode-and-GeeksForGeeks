class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left,Max,set_,Sum = 0,0,set(),0
        for right in range(len(nums)):
            while(nums[right] in set_):
                set_.discard(nums[left])
                Sum -= nums[left]
                left += 1
            set_.add(nums[right])
            Sum += nums[right]
            Max = max(Max,Sum)
        return Max
