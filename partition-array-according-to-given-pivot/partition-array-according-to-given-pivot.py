class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before,equal,after = [],[],[]
        for i in nums:
            if i>pivot:
                after.append(i)
            elif i==pivot:
                equal.append(i)
            elif i<pivot:
                before.append(i)
        nums.clear()
        nums.extend(before)
        nums.extend(equal)
        nums.extend(after)
        return nums