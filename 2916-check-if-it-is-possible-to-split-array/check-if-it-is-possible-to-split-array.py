class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums)<=2:
            return True
        for i in range(len(nums)-1):
            if nums[i]+nums[i+1]>=m:
                return True
        return False
        
                    
            
        