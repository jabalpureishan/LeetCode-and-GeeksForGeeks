#User function Template for python3

class Solution:
    def maxVal(self, a, n):
        Max = -1
        Min = 10**5 + 2
        for i in range(n):
            Max = max(a[i]-i,Max)
            Min = min(a[i]-i,Min)
        return Max - Min
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maxVal(a, n))

        T -= 1


if __name__ == "__main__":
    main()





# } Driver Code Ends