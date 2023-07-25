
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        right,LMax,RMax,length = {},-1,-1,len(arr)
        for i in arr[1:]:
            RMax = max(RMax,i)
            right[i] = right.get(i,0) + 1
        for i in range(length):
            #print("i:",i)
            #print("right:",right,"RM",RMax)
            #print("left:",LMax)
            if i==0:
                if arr[0]>RMax:
                    return 0
            elif i==length-1:
                if arr[-1]>LMax:
                    return i
            else:
                right[arr[i]] -= 1
                if right[arr[i]]==0:
                    right.pop(arr[i])
                    if arr[i]==RMax:
                        RMax = max(right)
                if arr[i]>LMax and arr[i]>RMax:
                    return i

            LMax = max(LMax,arr[i])