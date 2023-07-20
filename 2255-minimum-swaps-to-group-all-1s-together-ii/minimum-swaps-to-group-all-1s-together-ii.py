class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        length = len(nums)
        window = nums.count(1)
        if window==0:
            return 0
        Min = length - window
        slides = length - window
        d = {0:0,1:1}
        for i in nums[:window]:
            d[i] += 1 
        for i in range(2*length):
            d[nums[window%length]] += 1
            d[nums[i%length]] -= 1
            window += 1
            Min = min(Min,d.get(0,0))
        return Min