#User function Template for python3
class Solution:
	def countPairs(self, mat1, mat2, n, x):
        p1x,p1y = 0,0
        n = len(mat2)
        p2x,p2y = n-1,n-1
        count = 0
    
    
        while p1x<n and p1y<n and p2x>=0 and p2y>=0:
    
            #print(mat1[p1x][p1y],mat2[p2x][p2y],p1x,p1y,p2x,p2y)
            sum_ = mat1[p1x][p1y] + mat2[p2x][p2y]
            #print("sum:",sum_)
            if sum_<x:
                p1y += 1
                if p1y==n:
                    p1y = 0
                    p1x += 1
            elif sum_>x:
                p2y -= 1
                if p2y==-1:
                    p2y = n-1
                    p2x -= 1
            else:
                #print("sum==x")
                count += 1
                p1y += 1
                if p1y==n:
                    p1y = 0
                    p1x += 1
                p2y -= 1
                if p2y==-1:
                    p2y = n-1
                    p2x -= 1
            # if p1x==1 and p1y==2:
            #     break
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends