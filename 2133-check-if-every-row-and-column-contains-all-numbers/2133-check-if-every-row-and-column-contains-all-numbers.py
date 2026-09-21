class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)
        
        for i in range(n):
            row_set = set()
            col_set = set()
            for j in range(n):
                row_set.add(matrix[i][j])
                col_set.add(matrix[j][i])
            
            # If the number of unique elements isn't n, duplicates exist
            if len(row_set) != n or len(col_set) != n:
                return False
                
        return True