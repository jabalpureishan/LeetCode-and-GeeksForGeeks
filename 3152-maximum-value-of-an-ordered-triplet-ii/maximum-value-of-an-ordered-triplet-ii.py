class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n,MaxArr,RMax = len(nums),[],float("-inf")
        for i in range(-1,-n-1,-1):
            RMax = max(RMax,nums[i])
            MaxArr.append(RMax)
        LMax,ans = nums[0],0
        for i in range(1,n-1):
            #print(LMax,nums[i],MaxArr[-(i+2)],(LMax-nums[i])*MaxArr[-(i+2)])
            ans = max(ans,(LMax-nums[i])*MaxArr[-(i+2)])
            LMax = max(LMax,nums[i])
        return ans    