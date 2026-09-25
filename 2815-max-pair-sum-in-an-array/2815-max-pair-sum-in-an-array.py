class Solution:
    def maxSum(self, nums: list[int]) -> int:
        # Array to store the maximum number seen so far for each largest digit (1-9)
        max_val = [0] * 10
        ans = -1

        for num in nums:
            # Find the largest digit in the current number
            max_digit = max(int(d) for d in str(num))
            
            # If we've already seen a number with the same max digit, pair them
            if max_val[max_digit] > 0:
                ans = max(ans, num + max_val[max_digit])
            
            # Keep the largest number for this max digit category
            max_val[max_digit] = max(max_val[max_digit], num)

        return ans