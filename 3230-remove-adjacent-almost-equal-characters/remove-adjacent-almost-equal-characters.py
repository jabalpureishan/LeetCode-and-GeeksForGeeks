

class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        d = {}
        word = list(word)
        n = len(word)
        for i in range(26):
             d[alpha[i]] = i
        ind = count = 0
        while ind<n-1:
            or1 = ord(word[ind])
            or2 = ord(word[ind+1])
            if or1==or2:
                count += 1
                ind += 1
                
            elif or1+1==or2 or or1==or2+1:
                count += 1
                ind += 1
            ind += 1
        return count

#         conflict = [0]*n
#         for i in range(n):
#             nal = {alpha[min(25,d[word[i]]+1)],word[i],alpha[d[word[i]]-1]}
#             if i==0:
#                 if word[i+1] in nal:
#                     conflict[i] += 1
#             elif i==n-1:
#                 if word[i-1] in nal:
#                     conflict[i] += 1
#             else:
#                 if word[i+1] in nal:
#                     conflict[i] += 1
#                 if word[i-1] in nal:
#                     conflict[i] += 1
#         print(conflict)
#         count = 0
#         Max = 3
#         while Max>0:
#             count += 1
#             Max = conflict[0]+conflict[1]
#             ind = 0
#             for i in range(1,n):
#                 if i==n-1:
#                     sum_ = conflict[n-1]+conflict[n-2]
#                     if sum_>Max:
#                         Max = sum_
#                         ind = i
#                 else:
#                     sum_ = conflict[i]+conflict[i-1]+conflict[i+1]
#                     if sum_>Max:
#                         Max = sum_
#                         ind = i
#             print("Max:",Max,"ind:",ind)
#             # if Max<=0:
#             #     break
#             # count += 1

#             if ind==0:
#                 conflict[ind] = max(0,conflict[ind]-2)
#                 conflict[ind+1] = max(0,conflict[ind+1]-1)
#             elif ind==n-1:
#                 conflict[ind] = max(0,conflict[ind]-2)
#                 conflict[ind-1] = max(0,conflict[ind-1]-1)
#             else:
#                 conflict[ind] = max(0,conflict[ind]-2)
#                 conflict[ind-1] = max(0,conflict[ind-1]-1)
#                 conflict[ind+1] = max(0,conflict[ind+1]-1)
#             print("conflict:",conflict)
#             print("------------")
#         return count
        
#         # word = list(word)
#         # n = len(word)
#         # for i in range(1,n):
#         #     if 
        