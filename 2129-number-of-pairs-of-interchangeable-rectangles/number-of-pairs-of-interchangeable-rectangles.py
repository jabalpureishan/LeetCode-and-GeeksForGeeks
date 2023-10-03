class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        d,count = {},0
        for i in rectangles:
            div = i[0]/i[1]
            count += d.get(div,0)
            d[div] = d.get(div,0) +1 
        return count
        