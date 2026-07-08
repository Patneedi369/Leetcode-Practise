class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        
        for r in range(len(matrix)):
            heapq.heappush(heap, (matrix[r][0], r, 0))

        for _ in range(k-1):
            val, r, c = heapq.heappop(heap)

            if c+1 < len(matrix):
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
        return heap[0][0] if heap else 0