class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        window = k
        slides = len(nums) - window
        ele =  {}
        Sum = 0
        for i in nums[:k]:
            Sum += i
            ele[i] = ele.get(i,0) + 1
        
        if len(ele)>=m:
            Max = Sum
        else:
            Max = 0
        for i in range(slides):
            Sum += nums[window]
            Sum -= nums[i]
            ele[nums[window]] = ele.get(nums[window],0) + 1
            ele[nums[i]] -= 1
            window += 1
            if ele[nums[i]]==0:
                ele.pop(nums[i])
            if len(ele)>=m:
                Max = max(Max,Sum)
        return Max

        