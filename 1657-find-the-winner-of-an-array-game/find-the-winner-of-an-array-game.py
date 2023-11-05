class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k>len(arr):
            return max(arr)            
        left = Max = 0
        right = 1
        winner = arr[0]
        d = {}

        while right<len(arr)-1 and Max<k:
            #print("curr:",arr[left],arr[right])
            if arr[left]>arr[right]:
                arr.append(arr[right])
                #print("new arr:",arr)
                #print("increase:",arr[left])
                d[arr[left]] = d.get(arr[left],0) + 1
                if d[arr[left]]>Max:
                    Max,winner = d[arr[left]],arr[left]
                right += 1
            else:
                arr.append(arr[left])
                #print("new arr:",arr)
                #print("increase:",arr[right])
                d[arr[right]] = d.get(arr[right],0) + 1
                if d[arr[right]]>Max:
                    Max,winner = d[arr[right]],arr[right]
                left = right
                right += 1
        
        return winner
        