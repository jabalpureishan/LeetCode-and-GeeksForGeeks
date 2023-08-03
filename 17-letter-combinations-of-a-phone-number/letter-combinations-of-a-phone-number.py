class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        length = len(digits)
        out = []
        if length==1:
            for i in d[digits]:
                out.append(i)
        elif length==2:
            for i in d[digits[0]]:
                for j in d[digits[1]]:
                    out.append(i+j) 
        elif length==3:
            for i in d[digits[0]]:
                for j in d[digits[1]]:
                    for k in d[digits[2]]:
                        out.append(i+j+k)
        elif length==4:
            for i in d[digits[0]]:
                for j in d[digits[1]]:
                    for k in d[digits[2]]:
                        for l in d[digits[3]]:
                            out.append(i+j+k+l)

        return out