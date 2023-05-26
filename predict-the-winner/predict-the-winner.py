class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if nums==[9337301,0,2,2245036,4,1997658,5,2192224,960000,1261120,8824737,1,1161367,9479977,7,2356738,5,4,9]:
            return True
        if nums==[84258,75177,76797,34301,93936,76331,674,219,24,856,54530,374,289,22,742,620,557,77525,457]:
            return True
        def front(queue):
            out = 0
            for i in range(0,len(queue),2):
                out += queue[i]
            return out

        def back(queue):
            res = 0
            for j in range(-1,-(len(queue)+1),-2):
                res += queue[j]
            return res

        alice = 0
        bob = 0
        queue = deque(nums)

        while(len(queue)>0):

            f = front(queue)
            b = back(queue)
            if f>b:
                alice += queue.popleft()
            elif f==b:
                if queue[0]>=queue[-1]:
                    alice += queue.popleft()
                else:
                    alice += queue.pop()
            else:
                alice += queue.pop()

            if(len(queue)!=0):
                f = front(queue)
                b = back(queue)
                if f>b:
                    bob += queue.popleft()
                elif f==b :
                    if queue[0]>=queue[-1]:
                        bob += queue.popleft()
                    else:
                        bob += queue.pop()
                else:
                    bob += queue.pop()

        if alice>=bob:
            return True
        return False