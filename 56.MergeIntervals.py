class Solution:
    def merge(intervals):
        intervals.sort(key = lambda x:x[0])
        left = True
        copy = []
        while(left):
            copy = []
            print("*")
            for i in range(len(intervals)-1):
                if intervals[i][1]<=intervals[i+1][0] :
                    copy.append([intervals[i][0],intervals[i+1][1]])
                    copy.extend(intervals[i+2:0])
                    break
            else:
                left = False


    print(merge([[1,3],[2,6],[8,10],[15,18]]))
    print(merge([[1,4],[4,5]]))