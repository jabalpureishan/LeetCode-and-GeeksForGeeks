"""
! the time complexity of this code is O(n^2) and gives TLE
! approach - hard brute force
"""
class Solution:
    def score(nums):
        mark = set()
        length = len(nums)
        score = 0 
        Min = float("inf")
        index = None
        while(len(mark)<length):
            Min = float("inf")
            index = None
            for i in range(length):
                if i not in mark:
                    if nums[i]<Min:
                        Min = nums[i]
                        index = i
            score += Min
            mark.add(index)
            if index==0:
                mark.add(index+1)
            elif index==(length-1):
                mark.add(index-1)
            else:
                mark.add(index+1)
                mark.add(index-1)
        return score

    print(score([2,3,5,1,3,2]))
    print(score([2,1,3,4,5,2]))


