class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        slow,shigh = list(str(low)),list(str(high))
        nlow,nhigh = len(slow),len(shigh)
        ans = []
        curr = 1
        for i in range(nlow):
            slow[i] = str(curr)
            curr += 1
        #print("slow:",slow)
        var = "".join(slow)
        new = int(var)
        ans = []
        also = nlow*"1"
        addition = int(also)
        for i in range(nlow,nhigh+1):
            if new in range(low,high+1):
                ans.append(new)
            while new%10<9:
                new += addition
                if new in range(low,high+1):
                    ans.append(new)
            also += "1"
            addition = int(also)
            var += str(int(var[-1])+1)
            new = int(var)
            #print(new,var,addition)
        return ans
            