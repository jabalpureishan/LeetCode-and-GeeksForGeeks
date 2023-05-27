class Solution:
    def findScore(self, nums: List[int]) -> int:
        new = sorted(nums)
        length = len(nums)
        d ={}
        i = 0
        for j in nums:
            if j in d:
                d[j].append(i)
            else:
                d[j] = deque([i])
            i += 1
        mark = set()
        score = 0
        index = None
        while(len(mark)<length):
            for i in new:
                index = (d.get(i))[0]
                d.get(i).popleft()
                if index not in mark:
                    score += i
                    mark.add(index)
                    if index==0:
                        mark.add(index+1)
                    elif index==(length-1):
                        mark.add(index-1)
                    else:
                        mark.add(index+1)
                        mark.add(index-1)
        return score