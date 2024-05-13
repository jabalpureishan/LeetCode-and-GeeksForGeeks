class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        r,c = len(grid),len(grid[0])
        total = 0
        for ind,i in enumerate(grid):
            actual = flipped = 0
            power = c-1
            for j in i:
                if j==0:
                    flipped += 2**power
                else:
                    actual += 2**power
                    
                power -= 1
            if flipped>actual:
                total += flipped
                for j in range(c):
                    if grid[ind][j]==0:
                        grid[ind][j] = 1
                    else:
                        grid[ind][j] = 0
            else:
                total += actual
        for i in range(c):
            temp = total
            for j in range(r):
                if grid[j][i]:
                    temp -=  2**(c-i-1)
                else:
                    temp += 2**(c-i-1)
            total = max(temp,total)
        return total
        