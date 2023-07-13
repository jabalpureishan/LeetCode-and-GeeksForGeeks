class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        S = sum(nums[:k])
        Max = S/k
        slides  = len(nums) - k
        window = k 
        #print("s--:",S)
        for i in range(slides):
            S += nums[window]
            S -= nums[i]
            #print("s:",S)
            Max = max(Max,S/k)
            window += 1
        return Max
