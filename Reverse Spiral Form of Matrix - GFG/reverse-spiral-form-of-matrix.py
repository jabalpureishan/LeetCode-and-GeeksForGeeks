#User function Template for python3
class Solution:
	def reverseSpiral(self, R, C, a):
        matrix = a
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
        return output[::-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C=[int(x) for x in input().split()]
        a=[[0]*C for c in range(R)]
        arr=input().split()
        for i in range(R*C):
            a[i//C][i%C]=int(arr[i])
            
        ob=Solution()
        ans=ob.reverseSpiral(R,C,a)
        for i in range(len(ans)):
            print(ans[i],end=" ")
            
        print()
# } Driver Code Ends