class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        num = [0]*n
        done = count = 0
        for ind,val in enumerate(flips):
            curr = ind+1
            #print("num:",num)
            if num[ind]:
                done += curr
            num[val-1] = 1
            if val<=curr:
                done += val
            if done==(curr*(curr+1))//2:
                count += 1
            #print("done:",done)
        return count
        num = sum_ = count = 0
        n = len(flips)
        a = n-1
        for i in flips:
            sum_ += pow(2,a)
            a -= 1
            num += pow(2,n-i)
            if num>=sum_:
                count += 1
        return count
        