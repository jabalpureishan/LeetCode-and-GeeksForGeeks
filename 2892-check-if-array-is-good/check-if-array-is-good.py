class Solution:
    def isGood(self, nums: List[int]) -> bool:
        Max = max(nums)
        Sum = sum(nums)
        if nums.count(Max)!=2:
            return False
        Sum -= 2*Max
        Max -= 1
        if Sum!=((Max*(Max+1)))//2:
            return False
        return True
        
