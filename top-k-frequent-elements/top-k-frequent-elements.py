class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D,Output = {},[]
        for i in nums:
            D[i] = D.get(i,0) + 1
        SD = dict(sorted(D.items(),key = lambda x:x[1],reverse = True))
        for i in SD:
            Output.append(i)
            if k==1:
                break
            k-=1
        return Output