class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common,output,a,b = 0,[],set(),set()
        for i in range(len(A)):
            a.add(A[i])
            b.add(B[i])
            if B[i]==A[i]:
                common += 1
            else:
                if B[i] in a:
                    common += 1
                if A[i] in b:
                    common += 1
            output.append(common)
        return output