class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        left,d,Max,ele = 0,{},0,nums[0]
        for right in range(len(nums)):
            d[nums[right]] = d.get(nums[right],0) + 1
            Max = max(Max,d[nums[right]])
            while(((right-left+1)-Max)>k):
                #Max = max(Max,max(d.values()))
                #print(nums[left:right+1])
                d[nums[left]] -= 1
                if d[nums[left]]==0:
                    d.pop(nums[left])
                left += 1
            #Max = max(Max,max(d.values()))
            
        return Max

