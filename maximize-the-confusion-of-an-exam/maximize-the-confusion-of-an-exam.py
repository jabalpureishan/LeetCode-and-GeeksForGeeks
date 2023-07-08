class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        d = {"T":0,"F":0}
        Max = 0
        left = 0
        for right in range(len(answerKey)):
            d[answerKey[right]] += 1
            Min = min(d.get("T",0),d.get("F",0))
            while(Min>k):
                d[answerKey[left]] -= 1
                Min = min(d.get("T",0),d.get("F",0))
                left += 1
            Max = max(Max,d["T"]+d["F"])
        return Max