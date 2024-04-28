class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        rows,columns,ans = defaultdict(int),defaultdict(int),0
        for row,val in enumerate(grid):
            for col,value in enumerate(val):
                rows[row] += value
                columns[col] += value
        #print(rows,columns)
        for row,val in enumerate(grid):
            for col,value in enumerate(val):
                
                if value:
                    #print(row,col)
                    curr = max(rows[row]-1,0)*max(columns[col]-1,0)
                    #print("curr:",curr)
                    ans += curr
        return ans
        