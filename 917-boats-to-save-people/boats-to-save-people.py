class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        p1,p2,count = 0,len(people)-1,0
        while p1<=p2:
            if people[p1]+people[p2]<=limit:
                p1 += 1
            p2 -= 1
            count += 1
        #print(p1,p2)
        return count



        