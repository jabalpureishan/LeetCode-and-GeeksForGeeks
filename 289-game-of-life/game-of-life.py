class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        r = len(board)
        c = len(board[0])
        ans = []
        for i in range(r):
            ans.append([])
            for j in range(c):
                d = {1:0,0:0}
                if i>0:
                    d[board[i-1][j]] += 1 #up
                if i<r-1:
                    d[board[i+1][j]] += 1 # down
                if j>0:
                    d[board[i][j-1]] += 1 #left
                if j<c-1:
                    d[board[i][j+1]] += 1 #right
                if i<r-1 and j>0:
                    d[board[i+1][j-1]] += 1 #southwest
                if i<r-1 and j<c-1:
                    d[board[i+1][j+1]] += 1 #southeast
                if i>0 and j>0:
                    d[board[i-1][j-1]] += 1 #northwest
                if i>0 and j<c-1:
                    d[board[i-1][j+1]] += 1 #northeast
                if board[i][j]==1:
                    if d[1] in {2,3}:
                        ans[i].append(1)
                    else:
                        ans[i].append(0)
                else:
                    if d[1]==3:
                        ans[i].append(1)
                    else:
                        ans[i].append(0)
        board.clear()
        for i in ans:
            board.append(i)