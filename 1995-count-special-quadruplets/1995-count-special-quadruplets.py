from collections import defaultdict
from typing import List

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        diff_count = defaultdict(int)
        
        # Iterate b backwards from n - 3 down to 1
        for b in range(n - 3, 0, -1):
            c = b + 1
            # Add all valid (nums[d] - nums[c]) where d > c
            for d in range(c + 1, n):
                diff_count[nums[d] - nums[c]] += 1
            
            # Count matching pairs nums[a] + nums[b]
            for a in range(b):
                ans += diff_count[nums[a] + nums[b]]
                
        return ans