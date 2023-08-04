class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(first,second):
            if second in first:
                return first
            Min = min(len(first),len(second))
            for i in range(Min,0,-1):
                if first[-i:]==second[0:i]:
                    first += second[i:]
                    break
            else:
                first += second
            return first
        results = (merge(merge(a,b),c),merge(merge(a,c),b),merge(merge(b,a),c), merge(merge(b,c),a),merge(merge(c,a),b),merge(merge(c,b),a),)
        out = tuple(filter(lambda x:len(x)==(len(min(results,key=lambda x:len(x)))),results))
        return min(out)
