import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = Counter(s)
        heap = []
        
        for key, count in hashmap.items():
            heapq.heappush(heap, (-count, key))
            
        result = []
        prev = None
        
        while heap:
            count, ch = heapq.heappop(heap)
            result.append(ch)
            
            if prev:
                heapq.heappush(heap, prev)
                prev = None
                
            if count + 1 < 0:
                prev = (count + 1, ch)
                
        res_str = "".join(result)
        return res_str if len(res_str) == len(s) else ""