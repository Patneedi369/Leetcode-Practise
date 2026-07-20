class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        total = m * n
        k = k % total

        result = [[0]*n for _ in range(m)]

        for i in range(total):
            old_r, old_c = i // n, i % n
            
            # Calculate new coordinates after shifting k steps
            new_index = (i + k) % total
            new_r, new_c = new_index // n, new_index % n
            
            result[new_r][new_c] = grid[old_r][old_c]
        return result