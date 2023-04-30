class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        Max = max(nums)
        Max = Max*k
        k -= 1
        Sum = (k*(k+1))//2
        return Max + Sum
        