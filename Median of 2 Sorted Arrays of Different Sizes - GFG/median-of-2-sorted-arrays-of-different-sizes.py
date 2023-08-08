#User function Template for python3

class Solution:
    def MedianOfArrays(self, array1, array2):
        array = array1+array2
        array.sort()
        length = len(array)
        if length&1==0:
            ans = (array[length//2]+array[length//2 - 1])/2
            if str(ans)[-2:]==".0":
                return int(ans)
            else:
                return ans
        else:
            return array[(length-1)//2]


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends