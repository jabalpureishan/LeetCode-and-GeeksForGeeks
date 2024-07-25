from collections import defaultdict
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for ind,val in enumerate(nums):
            curr = list(str(val))
            for i,j in enumerate(curr):
                curr[i] = str(mapping[int(j)])

            curr = int("".join(curr))
            d[curr].append(val)
        d = sorted(d.items())
        ans = []
        for i in d:
            ans.extend(i[1])
        return ans
                

        