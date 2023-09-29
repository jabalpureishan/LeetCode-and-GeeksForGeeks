class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        ans = []
        while set(d.values())!={0} :
            curr = []
            for i in d:
                if d[i]!=0:
                    curr.append(i)
                    d[i] -= 1
            ans.append(curr)
        return ans
        