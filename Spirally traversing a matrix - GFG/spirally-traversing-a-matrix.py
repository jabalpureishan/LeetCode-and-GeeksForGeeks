#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        columns = len(matrix[0])
        rows = len(matrix)
        #angle = ("right","down","left","up")
        #curr = 0
        direction = "right"
        done = set()
        a,b = 0,0
        output = []
        for i in range(columns*rows):
            curr = (a,b)
            output.append(matrix[a][b])
            #print("output:",output,"curr:",curr,"direction:",direction)
            if direction=="right":
                if((b+1==columns) or ((a,b+1) in done)):
                    direction="down"
                    a += 1
                else:
                    b += 1
            elif direction=="down":
                if((a+1==rows) or ((a+1,b) in done)):
                    direction="left"
                    b -= 1
                else:
                    a += 1
            elif direction=="left":
                if((b-1==(-1)) or ((a,b-1) in done)):
                    direction="up"
                    a -= 1
                else:
                    b -= 1
            elif direction=="up":
                if((a-1==(-1)) or ((a-1,b) in done)):
                    direction="right"
                    b += 1
                else:
                    a -= 1
            #print("a",a,"b",b,"direction:",direction)
            done.add(curr)
            #pr
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends