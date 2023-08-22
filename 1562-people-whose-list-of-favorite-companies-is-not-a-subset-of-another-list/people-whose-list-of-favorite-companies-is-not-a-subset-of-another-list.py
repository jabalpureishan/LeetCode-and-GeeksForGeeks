class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        subsets,ans,length = set(),[],len(favoriteCompanies)
        for i in range(length):
            for j in range(length):
                if j!=i:
                    if set(favoriteCompanies[i]).issubset(set(favoriteCompanies[j])):
                        break
            else:
                ans.append(i)
        return ans
