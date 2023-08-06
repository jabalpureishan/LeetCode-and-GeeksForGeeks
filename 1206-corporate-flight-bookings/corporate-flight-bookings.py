class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        output,Sum = [0]*n,0
        for i in bookings:
            output[i[0]-1] += i[2]
            if i[1]<n:
                output[i[1]] -= i[2]
        for i in range(n):
            Sum += output[i]
            output[i] = Sum
        return output