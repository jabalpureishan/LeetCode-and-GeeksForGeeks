class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_,Max,Zero = 0,0,False
        for i in nums:
            if i==0:
                Zero = True
            sum_ += i
            Max = max(Max,i)
        ans = (Max*(Max+1))//2 - sum_
        if ans==0 and Zero:
            return Max + 1
        return ans
        