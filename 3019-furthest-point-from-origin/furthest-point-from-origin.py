class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count,ans,space = {"L":0,"R":0},0,0
        for i in moves:
            if i=="L":
                count["L"]+=1
            elif i=="R":
                count["R"] += 1
            else:
                space += 1
        if count["L"]>=count["R"]:
            ans += -1*space
        else:
            ans += space
        return abs(ans + -1*count["L"] + count["R"])
        