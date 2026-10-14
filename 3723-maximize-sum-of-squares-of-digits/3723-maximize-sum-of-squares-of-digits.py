class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = []
        for i in range(num):
            # Take the maximum possible digit for the current position
            digit = min(9, sum)
            res.append(str(digit))
            sum -= digit
        
        # If there is still remaining sum left over, it's invalid
        if sum > 0:
            return ""
            
        return "".join(res)