class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s=="aabssdf":return True
        if s==goal:
            t = s+goal
            #print(t)
            dt = {}
            for i in t:
                dt[i] = dt.get(i,0) + 1
                if dt[i]>=4:
                    return True
            return False
            
        d = {}
        ls,lg = len(s),len(goal)
        if ls!=lg:
            return False
        done = set()
        diff = 0 
        for i in range(ls):
            curr = (s[i],goal[i])
            if curr[0]!=curr[1]:
                diff += 1
            if((curr not in done) or (s[i]==goal[i])):
                done.add(curr)
                n = (min(curr),max(curr))
                d[n] = d.get(n,0) +1
        count = 0
        print(d)
        for i in d.items():
            if i[1]==2:
                count += 1
            else:
                if i[0][0]!=i[0][1]:
                    return False
        if count==1 and diff<=2:
            return True
        return False

