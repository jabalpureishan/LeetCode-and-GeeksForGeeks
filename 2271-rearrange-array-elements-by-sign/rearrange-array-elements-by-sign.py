class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos,neg,new = 0,1,[None]*n
        for i in nums:
            if i>0:
                new[pos] = i
                pos += 2
            else:
                new[neg] = i
                neg += 2
        return new
        