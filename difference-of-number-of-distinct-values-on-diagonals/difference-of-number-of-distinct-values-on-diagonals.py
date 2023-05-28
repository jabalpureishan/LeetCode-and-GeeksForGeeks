class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        columns = len(grid[0])
        Max = max(rows,columns)
        output = []
        for i in range(rows):
            output.append([])
            for j in range(columns):
                #print("i:",i,"j:",j,"element:",grid[i][j])
                if (i-1<0) or (j-1<0):
                    topleft = 0
                else:
                    topleft = set()
                    one,two = i,j
                    for k in range(Max):
                        one -= 1
                        two -= 1
                        
                        if one<0 or two<0:
                            break
                        topleft.add(grid[one][two])
                    #print("topleft:",topleft)
                    #topleft = len(topleft)
                if ((i+1)>=rows) or ((j+1)>=columns):
                    bottomright = 0
                else:
                    bottomright = set()
                    a,b = i,j
                    for q in range(Max):
                        a += 1
                        b += 1
                        if a>=rows or b>=columns:
                            break
                        bottomright.add(grid[a][b])
                    #print("bottomright:",bottomright)
                    #bottomright = len(bottomright)
                    
                #print("top",topleft,"bottom",bottomright)
                if topleft!=0:
                    topleft = len(topleft)
                if bottomright!=0:
                    bottomright = len(bottomright)
                res = abs(topleft-bottomright)
                output[i].append(res)
        #print("-----------")
        return output
        