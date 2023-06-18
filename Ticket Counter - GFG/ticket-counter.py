from collections import deque
class Solution:
    def distributeTicket(self, N : int, K : int) -> int:
        array = []
        for i in range(N):
            array.append(i+1)
        array = deque(array)
        last = array[0]
        while(len(array)>0):
            for i in range(0,K):
                if len(array)>0:
                    last = array.popleft()
                else:
                    break                
            for i in range(K):
                if len(array)>0:
                    last = array.pop()
                else:
                    break
        return last



#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    
    N, K = map(int, input().split())
    
    obj = Solution()
    res = obj.distributeTicket(N, K)
    
    print(res)
# } Driver Code Ends