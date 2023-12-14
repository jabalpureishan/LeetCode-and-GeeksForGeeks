class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        r,c = len(grid),len(grid[0])
        columns =[]
        count = 0
        rows = []
        for i in grid:
            d = {1:0,0:0}
            for j,k in enumerate(i):
                d[k] += 1
                if len(columns)<=j:
                    columns.append({1:0,0:0})
                columns[j][k] += 1
            rows.append(d)
        #return columns,rows
        ans = []
        for i,j in enumerate(grid):
            ans.append([])
            for k,l in enumerate(j):
                ans[i].append(rows[i][1]+columns[k][1]-rows[i][0]-columns[k][0])

        return ans
    
        
        