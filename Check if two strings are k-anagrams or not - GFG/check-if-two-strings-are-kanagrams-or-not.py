#User function template for Python 3

class Solution:
    def areKAnagrams(self, str1, str2, k):
        d1,d2,len1,len2,diff = {},{},len(str1),len(str2),0
        if len1!=len2:
            return False
        for i in range(len1):
            d1[str1[i]] = d1.get(str1[i],0) + 1  
            d2[str2[i]] = d2.get(str2[i],0) + 1
        for i in d1:
            
            diff += max(0,d1[i] - d2.get(i,0))
        #print(d1,d2,diff)
        return diff<=k


#{ 
 # Driver Code Starts
#Initial template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        k = int(input())
        ob = Solution()
        if ob.areKAnagrams(arr[0], arr[1], k):
            print(1)
        else:
            print(0)
# } Driver Code Ends