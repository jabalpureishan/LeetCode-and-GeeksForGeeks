class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        new = nums[:]
        length = len(nums)
        new.sort(reverse=False)
        d = {}
        for i in range(length-k):
            curr = new[i]
            d[curr] = d.get(curr,0) + 1
        #print(d)
        out = []
        for i in nums:
            if i not in d:
                out.append(i)
            else:
                d[i] -= 1
                if d[i]==0:
                    d.pop(i)
        return out