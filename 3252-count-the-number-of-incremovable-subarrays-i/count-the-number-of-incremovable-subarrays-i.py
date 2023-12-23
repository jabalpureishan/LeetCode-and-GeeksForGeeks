class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1
        if n>=2:
            count += 2
        for i in range(1,n-1):
            slides = n-i+1
            window = i
            for j in range(slides):
                curr = nums[:j]+nums[window:]
                for k in range(1,len(curr)):
                    if curr[k]<=curr[k-1]:
                        break
                else:
                    count += 1
                window += 1
        return count
                    
        