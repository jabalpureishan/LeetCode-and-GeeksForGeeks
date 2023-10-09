from collections import deque
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        sums,d,length = {},{},len(nums)
        for i in range(length):
            if nums[i] not in d:
                d[nums[i]] = deque([i])
            else:
                d[nums[i]].append(i)
            sums[nums[i]] = sums.get(nums[i],0) + i
        #print(sums,d)
        for i in d:
            #print("i:",i)
            right,left,leni = sums[i],0,len(d[i])
            if leni==1:
                #print("is 1")
                d[i][0] = 0
            else:
                for j in range(leni):
                    temp = d[i][j]
                    right -= temp
                    #print(right,left)
                    d[i][j] = abs((leni-j-1)*d[i][j]-right) + abs(j*d[i][j]-left)
                    left += temp
        for i in range(length):
            temp = nums[i]
            nums[i] = d[nums[i]][0]
            d[temp].popleft()
        return nums
        