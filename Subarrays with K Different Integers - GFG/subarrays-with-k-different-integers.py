#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def subarrayCount(self, arr, N, k):

        def count(arr,N,k):            
            left,count,hashmap = 0,0,{}

            for right in range(N):
                hashmap[arr[right]] = hashmap.get(arr[right],0) + 1

                while(len(hashmap)>k):
                    hashmap[arr[left]] -= 1
                    if hashmap[arr[left]]==0:
                        hashmap.pop(arr[left])
                    left += 1
                count += right - left + 1
            return count

        return count(arr,N,k) - count(arr,N,k-1)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.subarrayCount(arr, N, k)
        print(res)
# } Driver Code Ends