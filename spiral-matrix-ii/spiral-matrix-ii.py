class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        direction = "right"
        done = set()
        a,b = 0,0
        output = []
        for i in range(n):
            output.append([])
            for j in range(n):
                output[i].append([0])
        for i in range(n*n):
            curr = (a,b)
            output[a][b] = i+1
            #print("output:",output,"curr:",curr,"direction:",direction)
            if direction=="right":
                if((b+1==n) or ((a,b+1) in done)):
                    direction="down"
                    a += 1
                else:
                    b += 1
            elif direction=="down":
                if((a+1==n) or ((a+1,b) in done)):
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