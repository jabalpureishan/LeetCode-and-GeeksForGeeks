class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = {}
        count = 0
        for i in nums:
            #print("i:",i)
            #print("hashmap:",hashmap)
            if i>=k:
                continue
            if i in hashmap:
                #print("i in map")
                count += 1
                hashmap[i] -= 1
                if hashmap[i]==0:
                    hashmap.pop(i)
                #print("after hashmap:",hashmap)
            else:
                #print("i not in map")
                hashmap[k-i] = hashmap.get(k-i,0) + 1
                #print("after hashmap:",hashmap)
        return count