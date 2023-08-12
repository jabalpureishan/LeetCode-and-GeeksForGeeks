class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        Sum = 0
        new = sorted(zip(reward1,reward2),reverse=True,key = lambda x:x[0]-x[1])
        for i in range(len(new)):
            if i<k:
                Sum += new[i][0]
            else:
                Sum += new[i][1]
        return Sum
