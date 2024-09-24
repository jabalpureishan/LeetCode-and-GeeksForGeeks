class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n,Min,Minnums = len(nums),float("inf"),[]
        for i in range(-1,-n-1,-1):
            Min = min(Min,nums[i])
            Minnums.append(Min)
        #Minnums = Minnums[::-1]
        Max,ans = nums[0],0
        for i in range(1,n-1):

            if Max<nums[i]<Minnums[-(i+2)]:
                ans += 2
            elif nums[i-1]<nums[i]<nums[i+1]:
                ans += 1
            Max = max(Max,nums[i])
        return ans   