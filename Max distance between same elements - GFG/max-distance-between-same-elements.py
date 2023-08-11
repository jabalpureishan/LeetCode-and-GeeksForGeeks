class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr, n):
        hashmap,Max = {},0
        for i in range(n):
            if arr[i] in hashmap:
                hashmap[arr[i]].append(i)
            else:
                hashmap[arr[i]] = [i]
        for i in hashmap:
            Max = max(Max,hashmap[i][-1]-hashmap[i][0])
        return Max



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.maxDistance(arr, n))
# Contrbuted By:Harshit Sidhwa


# } Driver Code Ends