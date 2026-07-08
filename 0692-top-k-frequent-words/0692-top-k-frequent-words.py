class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = Counter(words)
        heap = []
        ls = []

        for key, value in hashmap.items():
            heapq.heappush(heap, (-value,key))

        while len(ls)<k:
            freq, item = heapq.heappop(heap)
            ls.append(item)
        return ls