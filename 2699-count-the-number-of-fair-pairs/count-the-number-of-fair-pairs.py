class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        length = len(nums)

        def lessthanequalto(nums,k):
            count,left,right = 0,0,length-1
            
            while(left<right):
                Sum = nums[left] + nums[right]
                if Sum<=k:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            return count
        
        return lessthanequalto(nums,upper) - lessthanequalto(nums,lower-1)