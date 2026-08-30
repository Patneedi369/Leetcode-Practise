class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Identify left and right indices
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)
        
        # Option 1: Both from front
        option1 = right + 1
        
        # Option 2: Both from back
        option2 = n - left
        
        # Option 3: One from front, one from back
        option3 = (left + 1) + (n - right)
        
        return min(option1, option2, option3)