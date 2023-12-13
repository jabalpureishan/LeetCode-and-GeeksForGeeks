class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r,c = len(mat),len(mat[0])
        columns =[]
        count = 0
        rows = []
        for i in mat:
            d = {}
            for j,k in enumerate(i):
                d[k] = d.get(k,0) + 1
                if len(columns)<=j:
                    columns.append({1:0,0:0})
                columns[j][k] += 1
            rows.append(d)
        for i,j in enumerate(mat):
            for k,l in enumerate(j):
                if l==1:
                    if rows[i][1]==1 and columns[k][1]==1:
                        count += 1
        return count
        