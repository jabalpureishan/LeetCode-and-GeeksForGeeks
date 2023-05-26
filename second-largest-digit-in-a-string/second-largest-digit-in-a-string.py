class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set()
        for i in s:
            if i.isdigit():
                nums.add(i)
        if len(nums)<=1:
            return -1
        nums = list(nums)
        nums.sort()
        return int(nums[-2])