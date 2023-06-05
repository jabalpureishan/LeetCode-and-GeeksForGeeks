class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        length = len(coordinates)
        if length==2:
            return True
        y = coordinates[1][1]-coordinates[0][1]
        x = coordinates[1][0]-coordinates[0][0]
        if x==0 and y==0:
            slope = 0
        elif x==0:
            slope = float("inf")
        elif y==0:
            slope = 0
        else:
            slope = y/x

        for i in range(2,length):
            ydiff = coordinates[i][1]-coordinates[i-1][1]
            xdiff = coordinates[i][0]-coordinates[i-1][0]
            if xdiff==0 and ydiff==0:
                current = 0
            elif xdiff==0:
                current = float("inf")
            elif ydiff==0:
                current = 0
            else:
                current = ydiff/xdiff  
            if current!=slope:
                return False
        return True