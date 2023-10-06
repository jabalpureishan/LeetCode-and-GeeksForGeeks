class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans,i,j = [],king[0],king[1]
        queen = set()
        for k in queens:
            queen.add(tuple(k))

        while 0<=i<=7 and 0<=j<=7:
            if [i,j] in queens:
                ans.append([i,j])
                break
            j += 1#east
        i,j = king[0],king[1]
        while 0<=i<=7 and 0<=j<=7:
            if [i,j] in queens:
                ans.append([i,j])
                break
            j -= 1#west
        i,j = king[0],king[1]
        while 0<=i<=7 and 0<=j<=7:
            if [i,j] in queens:
                ans.append([i,j])
                break
            i += 1#south
        i,j = king[0],king[1]
        while 0<=i<=7 and 0<=j<=7:
            if [i,j] in queens:
                ans.append([i,j])
                break
            i -= 1#north
        i,j = king[0],king[1]
        while 0<=i<=7 and 0<=j<=7:
            if [i,j] in queens:
                ans.append([i,j])
                break
            i += 1#south-west
            j += 1
        i,j = king[0],king[1]
        while 0<=i<=7 and 0<=j<=7:
            if [i,j] in queens:
                ans.append([i,j])
                break
            i -= 1#north-west
            j -= 1
        i,j = king[0],king[1]
        while 0<=i<=7 and 0<=j<=7:
            if [i,j] in queens:
                ans.append([i,j])
                break
            i -= 1#north-east
            j += 1
        i,j = king[0],king[1]
        while 0<=i<=7 and 0<=j<=7:
            if [i,j] in queens:
                ans.append([i,j])
                break
            i += 1#soth-east
            j -= 1
        i,j = king[0],king[1]
        return ans
        