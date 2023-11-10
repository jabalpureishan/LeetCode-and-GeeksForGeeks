class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n,m = len(worker),len(difficulty)
        dans = pans= 0
        arr = zip(difficulty,profit)
        arr2 = zip(profit,difficulty)
        diff = sorted(arr,reverse=True)
        pro = sorted(arr2,reverse=True)
        worker.sort(reverse=True)
        dind = pind = 0
        """print("diff:",diff)
        print("pro:",pro)
        print("worker:",worker)"""
        for i in worker:
            print("i:",i)
            for j in range(dind,m):
                if diff[j][0]<=i:
                    dans += diff[j][1]
                    print("add:",diff[j][1])
                    dind = j
                    break
            for k in range(pind,m):
                if pro[k][1]<=i:
                    pans += pro[k][0]
                    print("add:",pro[k][0])
                    pind = k
                    break
        return max(dans,pans)