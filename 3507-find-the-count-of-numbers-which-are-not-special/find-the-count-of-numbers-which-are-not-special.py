class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        limit = floor(sqrt(r))
        sieve = [False,False]+[True]*(limit-1)
        ind = 2
        count = 0 
        while ind*ind<=r:
            if sieve[ind]:
                #print("ind:",ind)
                if ind*ind in range(l,r+1):
                    count += 1
                    #print("yes")
                for j in range(ind*ind,limit+1,ind):
                    sieve[j] = False
            ind += 1
        return r-l+1-count
        