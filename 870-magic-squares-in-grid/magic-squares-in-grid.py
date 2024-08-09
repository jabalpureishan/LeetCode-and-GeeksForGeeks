class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        count = 0
        for i in range(rows-2):
            for j in range(cols-2):
                row1 = grid[i][j] + grid[i+1][j] + grid[i+2][j]
                row2 = grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1]
                row3 = grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2]
                col1 = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                col2 = grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2]
                col3 = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                diag1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
                diag2 = grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]
                nums = {grid[i][j],grid[i][j+1],grid[i][j+2],
                        grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],
                        grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]}
                # print(nums)
                # print(row1,row2,row3,col1,col2,col3,diag1,diag2)
                if nums=={1,2,3,4,5,6,7,8,9} and row1==row2==row3 and col1==col2==col3 and diag1==diag2:
                    count += 1
        return count
        