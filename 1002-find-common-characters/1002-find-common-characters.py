from collections import Counter
from typing import List


class Solution:

  def commonChars(self, words: List[str]) -> List[str]:
    # Initialize minimum frequency counts with the first word's character counts
    min_freq = Counter(words[0])

    # Intersect frequencies with each subsequent word
    for word in words[1:]:
      min_freq &= Counter(word)

    # Expand the character counts into a list of characters
    return list(min_freq.elements())