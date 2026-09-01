class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        element_count = [0]*1001
        for num in target:
            element_count[num] += 1
        for num in arr:
            element_count[num] -= 1
        
        return all(c==0 for c in element_count)

        # Time Complexity: O(N)
        # Space Complexity: O(1) — constant extra space since the array size is fixed at 1001 regardless of input length.