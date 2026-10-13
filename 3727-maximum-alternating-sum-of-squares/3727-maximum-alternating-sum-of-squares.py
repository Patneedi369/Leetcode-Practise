class Solution:

  def maxAlternatingSum(self, nums: List[int]) -> int:
    # Square each element and sort them
    squares = sorted([x**2 for x in nums])
    n = len(squares)

    # The first half (smaller elements) are subtracted, the second half added
    mid = n // 2
    return sum(squares[mid:]) - sum(squares[:mid])