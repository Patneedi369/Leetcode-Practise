class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        pointer = len(nums) - 1
        res = [0]*(pointer+1)

        while left<=right:
            if nums[left]**2 > nums[right]**2:
                res[pointer] = nums[left]**2
                left += 1
            else:
                res[pointer] = nums[right]**2
                right -= 1
            pointer -= 1
        
        return res

