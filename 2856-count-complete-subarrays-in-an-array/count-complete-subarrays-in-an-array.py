class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))

        def count(nums,k):

            total,left,hashmap = 0,0,{}

            for right in range(len(nums)):
                hashmap[nums[right]] = hashmap.get(nums[right],0) + 1

                while(len(hashmap)>k):
                    hashmap[nums[left]] -= 1
                    if hashmap[nums[left]]==0:
                        hashmap.pop(nums[left])
                    left += 1

                
                total += right - left + 1

            return total

        return count(nums,k) - count(nums,k-1)