class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a>0: heap.append([-a,"a"])
        if b>0: heap.append([-b,"b"])
        if c>0: heap.append([-c,"c"])
        ans = "dd"
        heapify(heap)
        while len(heap)>0:
            #print(heap)
            if ans[-1]==ans[-2]==heap[0][1]:
                big = heappop(heap)
                if len(heap)==0: break
                ans += heap[0][1]
                curr = heappop(heap)
                curr[0] += 1
                if -curr[0]>0: heappush(heap,curr)
                heappush(heap,big)
            else:
                ans += heap[0][1]
                curr = heappop(heap)
                curr[0] += 1
                if -curr[0]>0: heappush(heap,curr)
            # print(heap,ans)
            # print("_--------")
        return ans[2:]
        