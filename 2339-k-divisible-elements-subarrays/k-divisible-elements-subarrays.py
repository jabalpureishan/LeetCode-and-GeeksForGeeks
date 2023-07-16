class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        Max = l = count = 0
        pairs = 0
        length = len(nums)
        final = set()
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        minus = sum(d.values()) - len(d.values())
        for r in range(length):
            if nums[r]%p==0:
                count += 1
            while(count>k):
                if nums[l]%p==0:
                    count -= 1
                l += 1
            #print("curr:",nums[l:r+1])
            for i in range(l,r+1):
                #print(nums[i:r+1])
                final.add(tuple(nums[i:r+1]))
        return len(final)