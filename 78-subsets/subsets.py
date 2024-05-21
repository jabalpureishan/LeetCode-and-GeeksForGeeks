class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans,n = [[]],len(nums)
        for i in range(1,n+1):
            n = combinations(nums,i)
            for i in n:
                ans.append(list(i))
        return ans
        