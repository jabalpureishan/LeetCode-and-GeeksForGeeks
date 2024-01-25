class Solution:
    def smallestNumber(self, num: int) -> int:
        num = str(num)
        if num[0]=="-":
            num = list(num[1:])
            num.sort(reverse=True)
            return -int("".join(num))
        else:
            num = list(num)
            num.sort()
            ind = 0
            n = len(num)
            while ind<n and num[ind]=="0":
                ind += 1
            ind = min(ind,n-1)
            num[ind],num[0]=num[0],num[ind]
            return int("".join(num))