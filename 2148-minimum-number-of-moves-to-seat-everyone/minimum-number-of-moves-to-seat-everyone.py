class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        ans = 0
        for i,j in zip(sorted(seats),sorted(students)):
            ans += abs(j-i)
        return ans
        