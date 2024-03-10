class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        d1,d2 = {},{}
        for i in range(n):
            d1[nums1[i]] = d1.get(nums1[i],0) + 1
            d2[nums2[i]] = d2.get(nums2[i],0) + 1
        common = set()

        nikal1 = nikal2 = n//2
        for i in d1:
            nikal1 -= d1[i] - 1
            d1[i] = 1
        for i in d2:
            nikal2 -= d2[i] - 1
            d2[i] = 1
        #print(nikal1,nikal2)
        i = 0
        while i<n and (nikal1>0 or nikal2>0):
            if nums1[i] in d1 and nums1[i] in d2:
                #print("common:",nums1[i])
                if nikal1>nikal2:
                    nikal1 -= d1[nums1[i]]
                    d1.pop(nums1[i])
                    #print(d1)
                else:
                    nikal2 -= d2[nums1[i]]
                    d2.pop(nums1[i])
            i += 1
        
        #print(nikal1,nikal2,d1,d2)
        i = 0
        while nikal1>0:
            #print(nums1[i])
            if nums1[i] in d1:
                if d1[nums1[i]]>=nikal1:
                    d1[nums1[i]] -= nikal1
                    if d1[nums1[i]]==0:
                        d1.pop(nums1[i])
                    break
                else:
                    nikal1 -= d1[nums1[i]]
                    d1.pop(nums1[i])
            i += 1
        #print(nikal1,nikal2)
        i = 0
        while nikal2>0:
            if nums2[i] in d2:
                if d2[nums2[i]]>=nikal2:
                    d2[nums2[i]] -= nikal2
                    if d2[nums2[i]]==0:
                        d2.pop(nums2[i])
                    break
                else:
                    nikal2 -= d2[nums2[i]]
                    d2.pop(nums2[i])
            i += 1
        for i in d2:
            d1[i] = d1.get(i,0) + d2[i]
        return len(d1)
            