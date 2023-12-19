class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows,columns,ans = len(img),len(img[0]),[]
        for i in range(rows):
            ans.append([])
            for j in range(columns):
                sum_,count = img[i][j],1
                if i>0:
                    sum_ += img[i-1][j]#up
                    count += 1
                if i<rows-1:
                    sum_ += img[i+1][j]#down
                    count += 1
                if j>0:
                    sum_ += img[i][j-1]#left
                    count += 1
                if j<columns-1:
                    sum_ += img[i][j+1]#right
                    count += 1
                if i>0 and j<columns-1:
                    sum_ += img[i-1][j+1]#north-east
                    count += 1
                if i>0 and j>0:
                    sum_ += img[i-1][j-1]#norht-west
                    count += 1
                if i<rows-1 and j<columns-1:
                    sum_ += img[i+1][j+1]#south-east
                    count += 1
                if i<rows-1 and j>0:
                    sum_ += img[i+1][j-1]#south-west
                    count += 1
                #print(i,j,sum_,count)
                ans[i].append(sum_//count)
        
        return ans
            