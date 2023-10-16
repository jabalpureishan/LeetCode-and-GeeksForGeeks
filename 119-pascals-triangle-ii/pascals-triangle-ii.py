class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        length = 1
        while(len(ans)<rowIndex+1):
            if length==1:
                ans.append([1])
            elif length==2:
                ans.append([1,1])
            else:
                curr = [1]
                Sum = sum(ans[-1][:2])
                curr.append(Sum)
                window = 2
                for i in range(len(ans[-1])-2):
                    #print("Sum:",Sum)
                    Sum += ans[-1][window]
                    Sum -= ans[-1][i]
                    window += 1
                    curr.append(Sum)
                curr.append(1)
                ans.append(curr)
            length += 1
        return ans[-1]
        