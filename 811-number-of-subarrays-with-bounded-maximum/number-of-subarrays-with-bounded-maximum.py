from sortedcontainers import SortedList
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def co(nums,k):
            def maxmap(hashmap):
                if len(hashmap)==0:
                    return 0
                return max(hashmap)
            left,count,hashmap,Max = 0,0,{},-1
            for right in range(len(nums)):
                hashmap[nums[right]] = hashmap.get(nums[right],0) + 1
                Max = max(Max,nums[right])
                while(Max>k and left<right):
                    hashmap[nums[left]] -= 1
                    if hashmap[nums[left]]==0:
                        hashmap.pop(nums[left])
                    if hashmap.get(Max,-1)==-1:
                        Max = maxmap(hashmap)
                    left += 1
                if Max<=k:
                    count += right - left + 1
            return count

        return co(nums,right) - co(nums,left-1)