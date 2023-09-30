class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        Sum,Max,length = nums[-1],nums[-1],len(nums)
        for i in range(-2,-(length+1),-1):
            if Sum>=nums[i]:
                Sum += nums[i]
            else:
                Max = max(Max,Sum)
                Sum = nums[i]
        Max = max(Max,Sum)
        return Max
        