class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        out = set()
        for i in range(length):
            target = 0 - nums[i]
            set_ = set()
            for j in range(i+1,length):
                if nums[j] in set_:
                    res = [nums[i],target-nums[j],nums[j]]
                    out.add(tuple(sorted(res)))
                else:
                    set_.add(target-nums[j])
        return list(out)
        