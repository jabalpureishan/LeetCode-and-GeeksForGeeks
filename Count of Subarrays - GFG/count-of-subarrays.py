#User function Template for python3
class Solution:


	def countSubarray(self,arr, n, k):
        count,left,Max,hmap = 0,0,0,{}
        for right in range(len(arr)):
            hmap[arr[right]] = hmap.get(arr[right],0) + 1
            Max = max(Max,arr[right])
            while(Max>k and left<right):
                hmap[arr[left]] -= 1
                if hmap[arr[left]]==0:
                    hmap.pop(arr[left])
                    if arr[left]==Max:
                        Max = max(hmap)
                left += 1
            if Max<=k:
                count += right - left + 1
        return (n*(n+1))//2 - count


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, k=map(int, input().strip().split())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.countSubarray(arr, n, k)
        print(ans)
        tc=tc-1
# } Driver Code Ends