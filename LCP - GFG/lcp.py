#User function Template for python3

class Solution:
    def LCP(self,arr,n):
        Min = len(arr[0])
        for i in range(1,n):
            Min = min(Min,len(arr[i]))
        #print("Min:",Min)
        output = ""
        for i in range(Min):
            pick = arr[0][i]
            #print("pick:",pick)
            for j in range(1,n):
                #print("check:",arr[j][i])
                if arr[j][i]!=pick:
                    #print("break executed")
                    break
            else:
                output += pick
                #print("break not executed output:",output)
        if output == "":
            return -1
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs =int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[ x  for x in input().split()]
        obj=Solution()
        print(obj.LCP(arr,n))
# } Driver Code Ends