class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        hmap = Counter(nums)
        Max = 1
        hmap = sorted(hmap.items(),key=lambda x:x[0])
        hmap = dict(hmap)
        for i in hmap:
            if i==1:
                if hmap[i]%2==0:
                    hmap[i]-=1
                Max = max(Max,hmap[i])
                continue
            count = 0
            while hmap[i]>=2 and i*i in hmap:
                count += 2
                i = i*i
            count += 1
            Max = max(Max,count)
        if Max%2==0:
            Max -= 1
        return Max
            