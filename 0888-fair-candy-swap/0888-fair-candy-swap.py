class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        
        # Target difference needed for swap
        delta = (sumB - sumA) // 2
        
        # Convert Bob's sizes to a set for O(1) lookup
        bob_set = set(bobSizes)
        
        for x in aliceSizes:
            y = x + delta
            if y in bob_set:
                return [x, y]