class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count,start,end = 0,0,len(people)-1
        people.sort()
        #print("f",start,end)
        while(start<=end):
            Sum = people[start] + people[end]
            #print(start,end)
            if Sum<= limit:
                count += 1
                start += 1
                end -= 1
            else:
                if people[end]<=limit:
                    count += 1
                end -= 1
        return count