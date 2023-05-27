class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums = tuple(nums)
        output = set()
        length = len(nums)
        output.add(nums)
        for i in range(1,length):
            C = combinations(nums,i)
            for j in C:
                output.add(j)
        out = [[]]
        for i in output:
            out.append(list(i))
        return out