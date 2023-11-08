class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        for i in range(1,len(tiles)+1):
            ans.update(permutations(tiles,i))
        
        return len(ans)
        