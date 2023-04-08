#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        pos = []
        neg = []
        output = arr[:]
        arr.clear()
        for i in output:
            if i>0 :
                pos.append(i)
            else:
                neg.append(i)
        arr.extend(pos)
        arr.extend(neg)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends