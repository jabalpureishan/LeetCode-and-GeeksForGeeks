class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        out = ""
        length = 0
        Sum = 0
        for i in shifts:
            Sum += i
            length += 1
        move = [Sum]
        current = Sum

        for i in range(length-1):
            current = current - shifts[i]
            move.append(current)
        #print(move)
        for i in range(length):
            res = ord(s[i])+move[i]
            #print(res)
            if res>122:
                if ((res-122)%26)==0:
                    ans = res - (26 * ((res - 122) // 26))
                else:
                    ans = res - (26 * ((res - 122) // 26+1))
                #print(ans)
                """while(res>122):
                    res -= 26"""
                ans = chr(ans)
            else:
                ans = res
                ans = chr(ans)
            out += ans
        return out

