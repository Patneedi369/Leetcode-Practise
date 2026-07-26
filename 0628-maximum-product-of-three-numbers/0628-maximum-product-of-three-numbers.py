class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        
        # Case 1: Product of the three largest numbers
        product1 = nums[-1] * nums[-2] * nums[-3]
        
        # Case 2: Product of two smallest (negative) numbers and the largest number
        product2 = nums[0] * nums[1] * nums[-1]
        
        return max(product1, product2)