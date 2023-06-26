class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        def merge(left,right,total):
            a = left + right
            a.sort()
            total += sum(a[:k])
            return total

        #global total
        total =0
        left = costs[:candidates]
        right = costs[-candidates:]
        if len(costs)<=candidates*2:
            costs.sort()
            #print("this")
            return sum(costs[:k])
        heapify(left)
        heapify(right)
        #print("left:",left)
        #print("right:",right)
        A = candidates
        B = len(costs) - (candidates + 1)
        #print("A:",A,"B:",B)
        #print("--------------------")
        while(k>0):
            k-=1
            if left[0]<=right[0] :
                #print("left has a smaller element")
                total += heappop(left)
                #print("new total:",total)
                if A<=B:
                    heappush(left,costs[A])
                    #print("heap after pushing",costs[A],":",left)
                    A+=1
                    #print("A change:",A)
                else:
                    return merge(left,right,total)
            else:
                #print("right has a smaller element")
                total += heappop(right)
                #print("new total:",total)
                if A<=B:
                    heappush(right,costs[B])
                    #print("heap after pushing",costs[B],":",left)
                    B-=1
                    #print("B change:",B)
                else:
                    return merge(left,right,total)
            #print("----------------------------------------")
        return total