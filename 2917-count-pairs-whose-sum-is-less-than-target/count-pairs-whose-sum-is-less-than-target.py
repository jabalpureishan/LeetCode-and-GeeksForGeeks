class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left,right,count = 0,len(nums)-1,0
        while(left<right):
            Sum = nums[left] + nums[right]
            if Sum<target:
                left += 1
                count += right - left + 1
            else:
                right -= 1
        return count

                