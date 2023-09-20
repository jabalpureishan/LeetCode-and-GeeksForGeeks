class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target,left,Sum,Max,length = sum(nums) - x,0,0,0,len(nums)
        if target==0:
            return length
        for right in range(length):
            Sum += nums[right]
            #print("window:",nums[left:right+1])
            while(Sum>target and left<right):
                Sum -= nums[left]
                left += 1
            #print("window2:",nums[left:right+1])
            if Sum==target:
                #print("update")
                Max  = max(Max,right-left+1)
        if Max==0:
            return -1
        return length - Max
        