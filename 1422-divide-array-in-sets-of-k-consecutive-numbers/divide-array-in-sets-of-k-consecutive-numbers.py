from collections import Counter
from sortedcontainers import SortedDict
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n%k!=0:
            return False
        nums = SortedDict(Counter(nums))
        for i in range(n//k):
            for j in nums:
                break
            #print("j:",j)
            nums[j] -= 1
            if nums[j]==0:
                nums.pop(j)
            for m in range(j+1,j+k):
                #print("m",m)
                if m in nums:
                    nums[m] -= 1
                    if nums[m]==0:
                        nums.pop(m)
                else:
                    return False
            #print(nums)
        return True
        