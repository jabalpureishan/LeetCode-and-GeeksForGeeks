"""
!logic - we can use simple sliding window and update max when a new element comes in the
!        problem occurs when the array keeps decresing this. to tackle this whenever the 
!        max element leaves the window rescan the window to obtain max
"""
class Solution:
    def maxsub(arr,n,k):
        if k==1:
            return arr
        slides = n - k
        Max = max(arr[:k])
        output = [Max]
        window = k
        for j in range(slides):
            sub = arr[j]
            if sub==Max:
                Max = max(arr[j+1:window])
            Max = max(Max,arr[window])
            output.append(Max)
            window += 1
        return output

    print(maxsub([1,2,3,1,4,5,2,3,6],9,3))
    print(maxsub([8,5,10,7,9,4,15,12,90,13],10,4))
    print(maxsub([4,5,6,7,2,3,1,1],8,3))
    print(maxsub([1,2,3,4,5],5,1))