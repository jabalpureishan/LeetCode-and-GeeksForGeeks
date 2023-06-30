class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        rc = 0
        right = 0
        for i in nums:
            rc += 1
            right += i
        left,lc = 0,0
        Min = float("inf")
        ind = 0
        for i in nums:
            left += i
            lc += 1
            right -= i
            rc -= 1
            if lc==0:
                l = 0
            else:
                l = left//lc
            if rc==0:
                r = 0
            else:
                r = right//rc
            #print("l:",l,"r:",r)
            diff = abs(l-r)
            if Min>diff:
                Min = diff
                ind = lc - 1
            #print("Min:",Min)
        return ind