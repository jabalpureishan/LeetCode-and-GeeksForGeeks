class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        Set,count,pairs = set(),0,set()
        for i in nums:
            if i in Set:
                pairs.add((i-k,i))
            Set.add(i+k)
        return len(pairs)