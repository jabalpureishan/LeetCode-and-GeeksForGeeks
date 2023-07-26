class Solution:
    def smallestSubWithSum(self, a, n, x):
        nums = a
        target = x
        length = len(nums)
        left = 0
        sum_ = 0
        Min = float("inf")
        total = 0
        for right in range(length):
            total += nums[right]
            sum_ += nums[right]
            #print("sum:",sum_)
            while(sum_>target and left<right and sum_-nums[left]>target):
                sum_-= nums[left]
                #print("sumwh:",sum_)
                left += 1
                Min = min(Min,right-left+1)
                #print("Min:",Min)
            if sum_>target:
                Min = min(Min,right-left+1)
        if total==target:
            Min = min(Min,length)
        if Min==float("inf"):
            return 0
        return Min
        



#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends