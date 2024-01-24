class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        columns = len(grid[0])
        upar = sum(grid[0][1:])
        niche = 0
        Min =  Min = min(float("inf"),max(upar,niche))
        for i in range(1,columns):
            #print(upar,niche)
            Min = min(Min,max(upar,niche))

            upar -= grid[0][i]
            niche += grid[1][i-1]
            Min = min(Min,max(upar,niche))
        return Min
        