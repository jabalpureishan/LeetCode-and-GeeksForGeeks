class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def fsieve(n):
            arr = []
            for i in range(n+1):
                arr.append(i)
            root = sqrt(n)
            i = 2
            while i<=root:
                if arr[i]==i:
                    for j in range(i*i,n+1,i):
                        if arr[j]>i:
                            arr[j] = i
                i += 1
            return arr
        arr = fsieve(1000)
        def primefacts(n,set_):
            while n!=1:
                set_.add(arr[n])
                n //= arr[n]
        set_ = set()
        for i in nums:
            primefacts(i,set_)
        return len(set_)
        