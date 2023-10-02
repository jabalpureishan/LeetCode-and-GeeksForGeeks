class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = []
        for i in range(n):
            mat.append([0]*n)
        #print(mat)
        for i in queries:
            #print(i)
            boundary = i[3]+1<n
            for j in range(i[0],i[2]+1):
                #print(j,i[1])
                mat[j][i[1]] += 1
                if boundary:
                    mat[j][i[3]+1] += -1
        for i in range(n):
            prefix = mat[i][0]
            for j in range(1,n):
                prefix += mat[i][j]
                mat[i][j] = prefix

        return mat
        