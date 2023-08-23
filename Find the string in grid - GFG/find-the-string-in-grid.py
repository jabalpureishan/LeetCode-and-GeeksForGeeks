#User function Template for python3

class Solution:
	def searchWord(self, grid, word):
        rows,columns,ans,length  = len(grid),len(grid[0]),[],len(word)
        for a in range(rows):
            for b in range(columns):
                if grid[a][b]==word[0]:

                    for i in range(8):
                        p,q = a,b
                        #up
                        if i==0:
                            for j in range(length):
                                if p==-1:
                                    break
                                if grid[p][q]==word[j]:
                                    p -= 1
                                else:
                                    break
                            else:
                                ans.append([a,b])
                                break
                        elif i==1:
                            for j in range(length):
                                if p==-1 or q==-1:
                                    break
                                if grid[p][q]==word[j]:
                                    p -= 1
                                    q -= 1
                                else:
                                    break
                            else:
                                ans.append([a,b])
                                break
                        elif i==2:
                            for j in range(length):
                                if p==-1 or q==columns:
                                    break
                                if grid[p][q]==word[j]:
                                    p -= 1
                                    q += 1
                                else:
                                    break
                            else:
                                ans.append([a,b])
                                break
                        elif i==3:
                            for j in range(length):
                                if q==columns:
                                    break
                                if grid[p][q]==word[j]:
                                    q += 1
                                else:
                                    break
                            else:
                                ans.append([a,b])
                                break
                        elif i==4:
                            for j in range(length):
                                if p==rows or q==columns:
                                    break
                                if grid[p][q]==word[j]:
                                    p += 1
                                    q += 1
                                else:
                                    break
                            else:
                                ans.append([a,b])
                                break
                        elif i==5:
                            for j in range(length):
                                if  p==rows:
                                    break
                                if grid[p][q]==word[j]:
                                    p += 1
                                else:
                                    break
                            else:
                                ans.append([a,b])
                                break
                        elif i==6:
                            for j in range(length):
                                if q==-1 or p==rows:
                                    break
                                if grid[p][q]==word[j]:
                                    p += 1
                                    q -= 1
                                else:
                                    break
                            else:
                                ans.append([a,b])
                                break
                        elif i==7:
                            for j in range(length):
                                if q==-1 :
                                    break
                                if grid[p][q]==word[j]:
                                    q -= 1
                                else:
                                    break
                            else:
                                ans.append([a,b])
                                break
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends