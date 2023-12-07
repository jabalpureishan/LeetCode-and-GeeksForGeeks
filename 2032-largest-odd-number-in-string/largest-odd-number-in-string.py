class Solution:
    def largestOddNumber(self, num: str) -> str:
      length = len(num)
      ind = -1
      #print("first:",num[ind])
      while ind>=-length and int(num[ind])%2==0:
          #print(num[ind])
          ind -= 1
      if ind==-1:
          return num
      return num[-length:ind+1]