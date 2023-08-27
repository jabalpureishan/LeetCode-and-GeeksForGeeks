class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        target = k
        arr,ans,set_ = [],[],set()
        for i in range(1,n+1):
            arr.append(i)
        i += 1
        for j in arr:
            if j in set_:
                arr.append(i)
                i += 1
            else:
                set_.add(target-j)
                ans.append(j)
        return sum(ans)