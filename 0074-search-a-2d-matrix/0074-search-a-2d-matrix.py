class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_size = len(matrix)
        column_size = len(matrix[0])

        top = 0
        bottom = row_size - 1

        while top <= bottom:
            mid = (top+bottom)//2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid
                break

        # If top moved past the last row, the target is too large to exist in the matrix
        if top >= row_size:
            return False
            
        left = 0
        right = column_size - 1

        while left <= right:
            mid = (left + right)//2

            if target == matrix[top][mid]:
                return True
            if target > matrix[top][mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False