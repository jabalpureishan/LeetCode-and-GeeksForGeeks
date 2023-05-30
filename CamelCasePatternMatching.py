class Solution:
    def camelcase(N,Dictionary,Pattern):
        #print(Pattern)
        lp = len(Pattern)
        out = []
        for i in Dictionary:
            curr = ""
            for j in i:
                if j.isupper():
                    curr += j
            #print(curr)
            lc = len(curr)
            #if lc<=lp:
                #if curr in Pattern:
                    #out.append(i)
            #else:
            if Pattern in curr:
                out.append(i)
        out.sort()
        if len(out)==0:
            return -1
        return out

    print(camelcase(3,["WelcomeGeek","WelcomeToGeeksForGeeks","GeeksForGeeks"],"WTG"))
    print(camelcase(8,["Hi","Hello","HelloWorld","HiTech","HiGeek","HiTechWorld","HiTechCity","HiTechLab"],"HA"))