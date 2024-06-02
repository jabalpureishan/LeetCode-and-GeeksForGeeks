class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        m = intervals
        m.sort()
        print(m)
        new = []
        start,end = m[0][0],m[0][1]
        for i in range(1,len(m)):
            if end>=m[i][0]:
                end = max(m[i][1],end)
            else:
                new.append([start,end])
                start,end = m[i][0],m[i][1]
        if len(new)==0 or new[-1]!=[start,end]:
            new.append([start,end])

        return new
        