class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        flag = False
        Sum = 0
        if length%2==0:
            loop = length//2
        else:
            flag = True
            loop = (length-1)//2
        #print("length:",length,"loop:",loop)
        for i in range(loop):
            #print(mat[i][i],mat[i][-(i+1)],mat[-(i+1)][i],mat[-(i+1)][-(i+1)])
            Sum += mat[i][i] + mat[i][-(i+1)] + mat[-(i+1)][i] + mat[-(i+1)][-(i+1)]
        if flag:
            Sum += mat[loop][loop]
        return Sum