class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # Base cases: 1 step -> 1 way, 2 steps -> 2 ways
        prev2, prev1 = 1, 2
        
        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
            
        return prev1