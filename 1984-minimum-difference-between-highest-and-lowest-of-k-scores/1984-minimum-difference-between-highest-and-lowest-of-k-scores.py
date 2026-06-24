class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        if len(nums)<2:
            return 0
        
        nums.sort()
        min_diff = float('inf')

        for i in range(k,len(nums)+1):

            diff = nums[i-1] - nums[i-k]
            min_diff = min(diff, min_diff)

        return min_diff