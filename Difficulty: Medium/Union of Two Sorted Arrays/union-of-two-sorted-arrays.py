#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        #arr2,arr1 = max(arr1,arr2,key = lambda x:len(x)),min(arr1,arr2,key = lambda x:len(x))
        ind1 = ind2 = 0
        ans = []
        def put(ans,ele):
            if len(ans)==0:
                ans.append(ele)
            elif ans[-1]!=ele:
                ans.append(ele)
            
        while ind1<n and ind2<m:
            #print(ind1,ind2)
            if ind1<n and  arr1[ind1]<=arr2[ind2]:
                    put(ans,arr1[ind1])
                    ind1 += 1          
            elif ind2<m:
                put(ans,arr2[ind2])
                ind2 += 1
        for i in range(ind1,n):
            if ans[-1]!=arr1[i]: ans.append(arr1[i])
        for i in range(ind2,m):
            if ans[-1]!=arr2[i]: ans.append(arr2[i])
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends