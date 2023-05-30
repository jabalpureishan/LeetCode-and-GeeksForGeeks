from collections import deque
class Solution:
    def predict(nums):

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




    print(predict([1,5,2]))
    print(predict([1,5,233,7]))
    print(predict([1,1]))
    print(predict([1]))
    print(predict([2,4,55,6,8]))
    print(predict([1,2,99]))