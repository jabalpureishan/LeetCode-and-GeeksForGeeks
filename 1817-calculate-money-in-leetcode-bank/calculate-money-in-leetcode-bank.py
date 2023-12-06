class Solution:
    def totalMoney(self, n: int) -> int:
        # if n<=7:
        #     return (n*(n+1))//2
        ans = 0
        div = n//7
        rem = n%7
        #print(div,rem
        
        ans += (56+(div-1)*7)*(div/2)
        #print(ans)
        rem += div
        ans += (rem*(rem+1))//2 - (div*(div+1))//2  
        return int(ans)
        