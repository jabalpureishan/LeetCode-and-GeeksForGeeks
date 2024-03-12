class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sum_ = 0
        hmap = {}
        Max = float("-inf")
        for j,i in enumerate(nums):
            sum_ += i
            #print(j,i,i-k,hmap)
            if i<0:
                curr1 = i+k
                curr2 = i-k
            else:
                curr1 = i-k
                curr2 = i+k
            ##print("curr:",curr)
            if curr1 in hmap:
                #print("in")
                if hmap[curr1]==0:
                    #print("sum_",sum_)
                    Max = max(Max,sum_)
                else:
                    Max = max(Max,sum_-nums[hmap[curr1]-1])
            if curr2 in hmap:
                #print("in2")
                if hmap[curr2]==0:
                    #print("sum_",sum_)
                    Max = max(Max,sum_)
                else:
                    Max = max(Max,sum_-nums[hmap[curr2]-1])
            if i not in hmap:
                hmap[i] = j
            elif nums[hmap[i]]>sum_:
                hmap[i] = j
            nums[j] = sum_
        if Max==float("-inf"):
            return 0
        return Max
        