class Solution:
    def originalDigits(self, s: str) -> str:
        s = Counter(s)
        ans = ""
        if "z" in s:
            ans += "0"*s["z"]
            s["e"] -= s["z"] 
            s["r"] -= s["z"]  
            s["o"] -= s["z"] 
            if s["e"]==0:
                s.pop("e")
            if s["r"]==0:
                s.pop("r")
            if s["o"]==0:
                s.pop("o")
            s.pop("z")
        if "w" in s:
            ans += "2"*s["w"]
            s["t"] -= s["w"]  
            s["o"] -= s["w"] 
            if s["t"]==0:
                s.pop("t")
            if s["o"]==0:
                s.pop("o")
            s.pop("w")
        if "x" in s:
            ans += "6"*s["x"]
            s["i"] -= s["x"]  
            s["s"] -= s["x"] 
            if s["i"]==0:
                s.pop("i")
            if s["s"]==0:
                s.pop("s")
            s.pop("x")
        if "u" in s:
            ans += "4"*s["u"]
            s["f"] -= s["u"] 
            s["r"] -= s["u"]  
            s["o"] -= s["u"] 
            if s["f"]==0:
                s.pop("f")
            if s["r"]==0:
                s.pop("r")
            if s["o"]==0:
                s.pop("o")
            s.pop("u")
        if "g" in s:
            ans += "8"*s["g"]
            s["e"] -= s["g"] 
            s["i"] -= s["g"]  
            s["h"] -= s["g"] 
            s["t"] -= s["g"] 
            if s["e"]==0:
                s.pop("e")
            if s["i"]==0:
                s.pop("i")
            if s["h"]==0:
                s.pop("h")
            if s["t"]==0:
                s.pop("t")
            s.pop("g")
        if "o" in s:
            ans += "1"*s["o"]
            s["e"] -= s["o"] 
            s["n"] -= s["o"]  
            if s["e"]==0:
                s.pop("e")
            if s["n"]==0:
                s.pop("n")
            s.pop("o")
        if "t" in s:
            ans += "3"*s["t"]
            s["e"] -= 2*s["t"] 
            s["h"] -= s["t"] 
            s["r"] -= s["t"]  
            if s["e"]==0:
                s.pop("e")
            if s["h"]==0:
                s.pop("h")
            if s["r"]==0:
                s.pop("r")
            s.pop("t")
        if "f" in s:
            ans += "5"*s["f"]
            s["i"] -= s["f"] 
            s["v"] -= s["f"] 
            s["e"] -= s["f"]  
            if s["i"]==0:
                s.pop("i")
            if s["v"]==0:
                s.pop("v")
            if s["e"]==0:
                s.pop("e")
            s.pop("f")
        if "s" in s:
            ans += "7"*s["s"]
            s["n"] -= s["s"] 
            s["v"] -= s["s"] 
            s["e"] -= 2*s["s"]  
            if s["n"]==0:
                s.pop("n")
            if s["v"]==0:
                s.pop("v")
            if s["e"]==0:
                s.pop("e")
            s.pop("s")
        if "i" in s:
            ans += "9"*s["i"]
            s["n"] -= 2*s["i"]  
            s["e"] -= s["i"]  
            if s["n"]==0:
                s.pop("n")
            if s["e"]==0:
                s.pop("e")
            s.pop("i")   
        return "".join(sorted(ans))
        