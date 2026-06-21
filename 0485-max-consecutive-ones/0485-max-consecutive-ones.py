class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_consecutive = 0
        consecutive_count = 0

        for num in nums:
            if num == 1:
                consecutive_count += 1
            else:
                consecutive_count = 0

            max_consecutive = max(max_consecutive, consecutive_count)
        
        return max_consecutive