class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        output = []
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        for i in d:
            if d.get(i)==1:
                output.append(i)
        return output