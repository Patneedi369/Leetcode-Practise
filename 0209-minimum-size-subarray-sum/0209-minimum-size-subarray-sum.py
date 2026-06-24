class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        current_sum = 0
        mc = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum >= target:
                    
                    mc = min(mc, right - left + 1)
                    current_sum -= nums[left]
                    left += 1

        return mc if mc != float('inf') else 0