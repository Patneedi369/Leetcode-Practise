class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        largest_in_maxheap = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, largest_in_maxheap)

        if len(self.min_heap) > len(self.max_heap):
            smallest_in_minheap = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -smallest_in_minheap)


    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0 