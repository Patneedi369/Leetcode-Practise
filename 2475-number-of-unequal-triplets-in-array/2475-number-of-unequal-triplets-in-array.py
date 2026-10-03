from collections import Counter

class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        freqs = Counter(nums)
        ans = 0
        left = 0
        right = len(nums)
        
        for freq in freqs.values():
            right -= freq
            ans += left * freq * right
            left += freq
            
        return ans