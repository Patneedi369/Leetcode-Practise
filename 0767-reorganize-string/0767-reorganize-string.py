class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = Counter(s)
        heap = []
        result = ''
        prev = None

        for key, count in hashmap.items():
            heapq.heappush(heap, (-count, key))
        
        while heap:
            count, ch = heapq.heappop(heap)
            if prev:
                if prev[1] != ch:
                    result += ch
                if prev[0]<-1: heapq.heappush(heap, (prev[0]+1, prev[1]))
            else:
                result += ch
            prev = [count, ch]
                
        return result if len(result) == len(s) else ""