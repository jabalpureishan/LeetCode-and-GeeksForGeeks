class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        nums = tasks
        def divide_number(n):
            if n % 3 == 0:
                return '3' * (n // 3)    
            for i in range(n // 3, -1, -1):
                remaining = n - i * 3
                if remaining % 2 == 0:
                    return '3' * i + '2' * (remaining // 2)
            return -1
        d,count = {},0
        for i in nums:
            d[i] = d.get(i,0) + 1
        for i in d:
            s = divide_number(d[i])
            if s==-1:
                return -1
            count += len(s)
        return count
        
        