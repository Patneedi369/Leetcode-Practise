class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_index = 0
        for fast_index in range(1, len(nums)):
            if nums[write_index] != nums[fast_index]:
                write_index += 1
                nums[write_index] = nums[fast_index]
        return write_index+1
            
