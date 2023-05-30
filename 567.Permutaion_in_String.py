from itertools import permutations
def  checkInclusion(s1,s2):
    P = permutations(s1)
    for i in P:
        i = "".join(i)
        if i in s2:
            return True
    return False
print(checkInclusion("ab","eidbaooo"))
print(checkInclusion("ab","eidboaoo"))