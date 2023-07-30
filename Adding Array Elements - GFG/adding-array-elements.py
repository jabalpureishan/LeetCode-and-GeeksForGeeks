from heapq import heapify,heappush,heappop
class Solution:
    def minOperations(self, arr, n, k):
        heapify(arr)
        count = 0
        while(arr[0]<k):
            if len(arr)>=1:
                first = heappop(arr)
            else:
                return -1
            if len(arr)>=1:
                second = heappop(arr)
            else:
                return -1
            heappush(arr,first+second)
            count += 1
        return count



#{ 
 # Driver Code Starts

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = Solution().minOperations(arr, n, k)
        print(ans)
        tc -= 1


# } Driver Code Ends