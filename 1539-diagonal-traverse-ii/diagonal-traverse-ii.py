class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        rows = len(nums)
        Max = 0
        d = {}
        for i in range(rows-1,-1,-1):
            col = len(nums[i])
            Max = max(Max,col)
            for j in range(col):
                sum_ = i + j
                if sum_ in d:
                    d[sum_].append(nums[i][j])
                else:
                    d[sum_] = [nums[i][j]]
        # print(Max)
        ans = []
        for i in range(rows+Max-1):
            ans.extend(d.get(i,[]))
        return ans

        