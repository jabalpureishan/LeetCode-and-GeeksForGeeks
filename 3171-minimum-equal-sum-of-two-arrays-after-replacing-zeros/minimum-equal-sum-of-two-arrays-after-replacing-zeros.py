class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1 = z2 = s1 = s2 = 0
        for i in nums1:
            if i==0:
                z1 += 1
                s1 += 1
            else:
                s1 += i
        for i in nums2:
            if i==0:
                z2 += 1
                s2 += 1
            else:
                s2 += i
        if z1==0:
            if z2==0:
                if s1==s2:
                    return s1
                return -1
            if s1<s2:
                return -1
        elif z2==0:
            if z1==0:
                return 0
            if s2<s1:
                return -1
        return max(s1,s2)
        