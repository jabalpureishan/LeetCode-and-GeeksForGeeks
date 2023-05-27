class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row = 0
        count = 0
        for i in range(len(mat)):
            current = mat[i].count(1)
            #print("curremt:",current)
            if current>count:
                count = current
                row = i
        return [row,count]