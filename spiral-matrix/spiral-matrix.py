class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        columns = len(matrix[0])
        rows = len(matrix)
        #angle = ("right","down","left","up")
        #curr = 0
        direction = "right"
        done = set()
        a,b = 0,0
        output = []
        for i in range(columns*rows):
            curr = (a,b)
            output.append(matrix[a][b])
            #print("output:",output,"curr:",curr,"direction:",direction)
            if direction=="right":
                if((b+1==columns) or ((a,b+1) in done)):
                    direction="down"
                    a += 1
                else:
                    b += 1
            elif direction=="down":
                if((a+1==rows) or ((a+1,b) in done)):
                    direction="left"
                    b -= 1
                else:
                    a += 1
            elif direction=="left":
                if((b-1==(-1)) or ((a,b-1) in done)):
                    direction="up"
                    a -= 1
                else:
                    b -= 1
            elif direction=="up":
                if((a-1==(-1)) or ((a-1,b) in done)):
                    direction="right"
                    b += 1
                else:
                    a -= 1
            #print("a",a,"b",b,"direction:",direction)
            done.add(curr)
            #pr
        return output