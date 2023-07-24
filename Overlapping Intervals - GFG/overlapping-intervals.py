class Solution:
	def overlappedInterval(self, Intervals):
	    intervals = Intervals
        intervals.sort(key = lambda x:x[0])
        length = len(intervals)
        intervals.append([float("inf"),0])
        #print(intervals)
        output = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(length):
            if intervals[i+1][0]<=end:
                end = max(end,intervals[i+1][1])
            else:
                output.append([start,end])
                start = intervals[i+1][0]
                end = intervals[i+1][1]
        return output


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends