class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid

            # If the left half is sorted AND target is within its bounds
            if nums[left] <= nums[mid] and nums[left] <= target < nums[mid]:
                right = mid - 1
            # If the right half is sorted AND target is within its bounds
            elif nums[mid] < nums[right] and nums[mid] < target <= nums[right]:
                left = mid + 1
            # Otherwise, target must be in the opposite/unsorted half
            elif nums[left] <= nums[mid]:
                left = mid + 1  # Left was sorted, so target is in the right half
            else:
                right = mid - 1 # Right was sorted, so target is in the left half
            
        return -1