class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup = -1
        missing = -1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                dup = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                missing = nums[i - 1] + 1
                
        # Edge case: if the missing number is at the very beginning or end
        if nums[0] != 1:
            missing = 1
        elif nums[-1] != len(nums):
            missing = len(nums)
            
        return [dup, missing]