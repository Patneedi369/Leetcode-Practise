class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        seen_sums = set()
        left, right = 0, len(nums) - 1
        
        while left < right:
            seen_sums.add(nums[left] + nums[right])
            left += 1
            right -= 1
            
        return len(seen_sums)