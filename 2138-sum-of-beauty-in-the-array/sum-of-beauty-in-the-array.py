from sortedcontainers import SortedList
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        sl = SortedList(nums[1:])
        Max = nums[0]
        n = len(nums)
        ans = 0
        for i in range(1,n-1):
            sl.remove(nums[i])
            print(Max,nums[i],sl[0])
            if Max<nums[i]<sl[0]:
                ans += 2
            elif nums[i-1]<nums[i]<nums[i+1]:
                ans += 1
            Max = max(Max,nums[i])
        return ans

        