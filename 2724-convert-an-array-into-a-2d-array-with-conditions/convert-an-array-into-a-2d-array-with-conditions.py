class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        ans = []
        while len(d)>0 :
            nikal = set()
            curr = []
            for i in d:
                curr.append(i)
                d[i] -= 1
                if d[i]==0:
                    nikal.add(i)
            ans.append(curr)
            for i in nikal:
                d.pop(i)
        return ans
        