from collections import Counter
from typing import List


class Solution:

  def maxFrequencyElements(self, nums: List[int]) -> int:
    counts = Counter(nums)
    max_freq = max(counts.values())

    # Sum all frequencies that are equal to the maximum frequency
    return sum(freq for freq in counts.values() if freq == max_freq)