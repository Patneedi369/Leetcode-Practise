class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)
        for r,c in reservedSeats:
            if 2<=c<=9:
                reserved[r].add(c)
        
        max_groups = n*2 #max possible groups assuming all rows are empty

        for r, seats in reserved.items():
            left = any(c in seats for c in (2,3,4,5))
            right = any(c in seats for c in (6,7,8,9))
            middle = any(c in seats for c in (4,5,6,7))
            
            if left and right and middle:
                max_groups -= 2  # 0 groups can sit here
            elif left or right or middle:
                max_groups -= 1  # Only 1 group can sit here instead of 2
        
        return max_groups
