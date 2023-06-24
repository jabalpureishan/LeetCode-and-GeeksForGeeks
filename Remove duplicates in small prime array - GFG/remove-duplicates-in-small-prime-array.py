class Solution:
    def removeDuplicates(self, arr):
        Set = set()
        output = []
        for i in arr:
            if i not in Set:
                output.append(i)
            Set.add(i)
        arr.clear()
        arr.extend(output)
        return arr
    


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().removeDuplicates(arr)
        for i in range(len(res)):
            print(res[i], end=" ")
        print('')


# } Driver Code Ends