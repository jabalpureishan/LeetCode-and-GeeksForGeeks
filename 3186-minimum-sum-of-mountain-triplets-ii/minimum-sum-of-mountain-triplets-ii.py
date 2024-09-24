class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n,MinArr,RMin = len(nums),[],float("+inf")
        for i in range(-1,-n-1,-1):
            RMin = min(RMin,nums[i])
            MinArr.append(RMin)
        #return MinArr
        LMin,ans = nums[0],float("inf")
        for i in range(1,n-1):
            #print(LMin,nums[i],MinArr[-(i+2)],LMin+nums[i]+MinArr[-(i+2)])
            if LMin<nums[i]>MinArr[-(i+2)]:
                ans = min(ans,LMin+nums[i]+MinArr[-(i+2)])
            LMin = min(LMin,nums[i])
        if ans==float("inf"):
            return -1
        return ans
        