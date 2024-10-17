class Solution:
    def maximumSwap(self, num: int) -> int:
        n,arr,basic = floor(log10(num)+1)-1,defaultdict(list),[]
        while num>0:
            basic.append(num%10)
            arr[num%10].append(n)
            n -= 1
            num //= 10
        basic = basic[::-1]
        curr = basic[-1]
        srt = sorted(basic,reverse=True)
        for ind,val in enumerate(basic):
            if val!=srt[ind]:
                curr = basic[ind]
                basic[ind] = srt[ind]
                break
        for i in range(len(basic)-1,-1,-1):
            #print(basic[i])
            if basic[i]==basic[ind]:
                #print("yes")
                basic[i] = curr
                break
        ans = 0
        n = len(basic)-1
        for i in basic:
            ans += i*(10**n)
            n -= 1
        return ans
        