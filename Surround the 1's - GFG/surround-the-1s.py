#User function Template for python3

class Solution:
	def Count(self, matrix):
        rows,final = len(matrix),0
        columns = len(matrix[0])
        for i in range(rows):
            
            for j in range(columns):
                count = 0
                if matrix[i][j]==1:
                    #print("current:",i,j)
                    if i!=0 and matrix[i-1][j]==0:
                        count += 1
                    if i!=0 and j!=0 and matrix[i-1][j-1]==0:
                        count += 1
                    if i!=0 and j!=columns-1 and matrix[i-1][j+1]==0:
                        count += 1
                    if j!=columns-1  and matrix[i][j+1]==0:
                        count += 1
                    if i!=rows-1 and j!=columns-1 and matrix[i+1][j+1]==0:
                        count += 1
                    if i!=rows-1 and matrix[i+1][j]==0:
                        count += 1
                    if j!=0 and i!=rows-1 and matrix[i+1][j-1]==0:
                        count += 1
                    if j!=0 and matrix[i][j-1]==0:
                        count += 1 
                #print("count:",count)
                if count%2==0 and count!=0:
                    final += 1
        return final


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.Count(matrix)
		print(ans)

# } Driver Code Ends