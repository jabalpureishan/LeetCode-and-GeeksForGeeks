#User function Template for python3

class Solution:
    def endPoints(self, matrix, R, C):
        direction = "right"
        a,b=0,0
        rows = R
        columns = C
        for i in range(R*C):

            #print("current:",a,b)
            if direction=="right":
                if matrix[a][b]==0:
                    #print("is zero")
                    if b+1==columns:
                        #print("out of matrix")
                        return [a,b]
                    else:
                        #print("not out of matrix")
                        b += 1
                else:
                    matrix[a][b]=0
                    direction = "down"
                    #print("not zero")
                    #print("new direction:",direction,a+1,b)
                    if a+1==rows:
                        #print("out of matrix")
                        return [a,b]
                    else:
                        #print("not out of matrix")
                        a += 1
            elif direction=="down":
                if matrix[a][b]==0:
                    #print("is zero")
                    if a+1==rows:
                        #print("out of matrix")
                        return [a,b]
                    else:
                        #print("not out of matrix")
                        a += 1
                else:
                    matrix[a][b]=0
                    direction = "left"
                    if b-1==-1:
                        #print("out of matrix")
                        return [a,b]
                    else:
                        #print("not out of matrix")
                        b -= 1
            elif direction=="left":
                if matrix[a][b]==0:
                    #print("is zero")
                    if b-1==-1:
                        #print("out of matrix")
                        return [a,b]
                    else:
                        #print("not out of matrix")
                        b -= 1
                else:
                    matrix[a][b]=0
                    direction = "up"
                    if a-1==-1:
                        #print("out of matrix")
                        return [a,b]
                    else:
                        #print("not out of matrix")
                        a -= 1
            elif direction=="up":
                if matrix[a][b]==0:
                    #print("is zero")
                    if a-1==-1:
                        #print("out of matrix")
                        return [a,b]
                    else:
                        #print("not out of matrix")
                        a -= 1
                else:
                    matrix[a][b]=0
                    direction = "right"
                    if b+1==columns:
                        #print("out of matrix")
                        return [a,b]
                    else:
                        #print("not out of matrix")
                        b += 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        ob = Solution()
        ans = ob.endPoints(matrix,r,c)
        print('(',ans[0],', ',ans[1],')',sep ='')

# } Driver Code Ends