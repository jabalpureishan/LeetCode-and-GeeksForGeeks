class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        arr = []
        ans = 0
        for j,i in enumerate(nums):
            ind = 0
            while i>0:
                if len(arr)==ind:
                    arr.append(defaultdict(int))
                rem = i%10
                #print("curr:",j - arr[ind].get(rem,0))
                #print(rem)
                ans += j - arr[ind].get(rem,0)
                arr[ind][rem] += 1
                #print(arr)
                i //= 10
                ind += 1
        return ans
        