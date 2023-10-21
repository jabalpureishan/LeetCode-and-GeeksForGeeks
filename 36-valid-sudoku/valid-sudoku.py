class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {1:set(),2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set(),9:set()}
        columns = {1:set(),2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set(),9:set()}
        boxes = {"1":set(),"2":set(),"3":set(),"4":set(),"5":set(),"6":set(),"7":set(),"8":set(),"9":set()}
        soduko = [["1","1","1","2","2","2","3","3","3"]
                 ,["1","1","1","2","2","2","3","3","3"]
                 ,["1","1","1","2","2","2","3","3","3"]
                 ,["4","4","4","5","5","5","6","6","6"]
                 ,["4","4","4","5","5","5","6","6","6"]
                 ,["4","4","4","5","5","5","6","6","6"]
                 ,["7","7","7","8","8","8","9","9","9"]
                 ,["7","7","7","8","8","8","9","9","9"]
                 ,["7","7","7","8","8","8","9","9","9"]]

        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele!=".":
                    if ele in rows[i+1]:
                        #print(ele,"found in boxes no.",soduko[i][j])
                        return False
                    if ele in columns[j+1]:
                        #print(ele,"found in boxes no.",soduko[i][j])
                        return False
                    if ele in boxes[soduko[i][j]]:
                        #print(ele,"found in boxes no.",soduko[i][j])
                        return False
                    rows[i+1].add(ele)
                    columns[j+1].add(ele)
                    boxes[soduko[i][j]].add(ele)
                    #print(rows,columns,boxes)
        
        
        return True
        