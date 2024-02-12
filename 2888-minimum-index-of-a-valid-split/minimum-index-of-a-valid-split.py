class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        hmap =  Counter(nums)
        dom = max(hmap,key=lambda x:hmap[x])
        left,right = 0,hmap[dom]
        for i,j in enumerate(nums):
            if j==dom:
                left += 1
                right -= 1
            if left*2>i+1 and right*2>n-i-1:
                return i
        return -1

        