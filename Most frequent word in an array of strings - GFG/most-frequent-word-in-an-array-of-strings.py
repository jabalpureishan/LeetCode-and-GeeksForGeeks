#User function Template for python3

class Solution:
    
    #Function to find most frequent word in an array of strings.
    def mostFrequentWord(self,arr,n):
        hmap,Max,MaxWord = {},0,""
        for i in arr:
            hmap[i] =hmap.get(i,0) + 1
            Max = max(Max,hmap[i])
        done = set()
        for i in arr:
            if i not in done:
                if hmap[i]==Max:
                    MaxWord = i
            done.add(i)
        return MaxWord



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[x for x in input().strip().split()]
        obj = Solution()
        print(obj.mostFrequentWord(arr,n))

# } Driver Code Ends