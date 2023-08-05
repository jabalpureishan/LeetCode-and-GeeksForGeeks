#User function Template for python3


class Solution():
    def longestString(self, arr, n):
        Min = ""
        arr.sort(reverse=True,key=lambda x:len(x))
        set_ = set(arr)
        for i in arr:
            for j in range(1,len(i)):
                if i[0:j] not in set_:
                    break
            else:
                Min = i
                break
        arr = list(filter(lambda x:((len(x)==len(Min)) and x!=Min),arr))
        for i in arr:
            for j in range(1,len(i)):
                if i[0:j] not in set_:
                    break
            else:
                Min = min(Min,i)
        return Min


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr,n))
# } Driver Code Ends