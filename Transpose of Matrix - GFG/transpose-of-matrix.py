#User function Template for python3

class Solution:
    def transpose(self, matrix, n):
        output = []
        for i in range(n):
            output.append([])
            for j in range(n):
                output[i].append(matrix[j][i])
        matrix.clear()
        matrix.extend(output)


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
        
    ob = Solution()
    ob.transpose(matrix, n)
    
    for row in matrix:
        print(*row)
    
# } Driver Code Ends