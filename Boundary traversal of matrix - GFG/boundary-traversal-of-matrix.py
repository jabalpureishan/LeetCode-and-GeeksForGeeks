#User function Template for python3

class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        out = []
        if n==1:
            for i in matrix:
                out.extend(i)
            return out
        if m==1:
            for i in matrix:
                out.extend(i)
            return out
        a,b = 0,0
        direction = "right"
        seen = set()
        while (a,b) not in seen:
            out.append(matrix[a][b])
            seen.add((a,b))
            if direction=="right":
                if b!=(m-1):
                    b+=1
                else:
                    direction="down"
                    a += 1
            elif direction=="down":
                if a!=(n-1):
                    a += 1
                else:
                    direction="left"
                    b -= 1
            elif direction=="left":
                if b!=0:
                    b -=1
                else:
                    direction = "up"
                    a -= 1
            elif direction=="up":
                if a!=0:
                    a -= 1
        return out


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends