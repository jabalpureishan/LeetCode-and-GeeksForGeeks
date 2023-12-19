class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        lenw,lenp = len(searchWord),len(products)
        products.sort()
        ans = []
        for i in range(1,lenw+1):
            ans.append([])
            j = 0
            while j<lenp and len(ans[i-1])<3:
                if products[j].startswith(searchWord[:i]):
                    ans[i-1].append(products[j])
                j += 1
        return ans
        