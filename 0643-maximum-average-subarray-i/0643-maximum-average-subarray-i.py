class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        window_sum = 0
        
        for i in range(0, k):
            window_sum += nums[i]
        
        max_sum = window_sum
        
        for i in range(k, len(nums)):
           window_sum -= nums[left]
           left += 1
           window_sum +=  nums[i]
           max_sum = max(max_sum, window_sum)
        
        return max_sum/k
