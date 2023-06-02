class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        output = ""
        for i in romans:
            if i<=num:
                output += romans[i]*(num//i)
                num  = num%i
        return output