class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum_ = left = Max = 0
        n = len(nums)
        for right in range(n):
            sum_ += nums[right]
            while nums[right]*(right-left+1)-sum_>k:
                sum_ -= nums[left]
                left += 1
            Max = max(Max,right-left+1)
        return Max
            
        # # print(n)
        # for i in range(n):
        #     sum_ += nums[i]
        #     prefix.append(sum_)
        # #print(prefix)
        # Max = 1
        # last = 0
        # for i in range(n-1,0,-1):
        #     j = i - 1
        #     sum_ = nums[j]
        #     #print("i:",i,"j:",j)
        #     #print("nums[i]",nums[i],"i-j:",i-j,"sum_:",sum_)
        #     while j>=last and nums[i]*(i-j)-sum_<=k:
        #         j -= 1
        #         sum_ += nums[j]
        #         #print("j:",j,"sum_",sum_)
        #     last = max(j,0)
        #     #print(i,"-->",j)
        #     Max = max(Max,i-j)
        #     # if i-j==n:
        #     #     return Max
        # return Max
