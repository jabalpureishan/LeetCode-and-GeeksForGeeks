class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count =left = total =  sum_ =  0
        n = len(nums)
        for right in range(n):
            sum_ += nums[right]
            total = sum_*(right-left+1)
            while total>=k:
                #print("undar")
                sum_ -= nums[left]
                left += 1
                total = sum_*(right-left+1)
                
            #print("total",total)
            count += right-left+1
        return count
        