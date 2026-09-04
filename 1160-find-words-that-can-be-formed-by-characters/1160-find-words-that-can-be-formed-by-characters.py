from collections import Counter
from typing import List


class Solution:

  def countCharacters(self, words: List[str], chars: str) -> int:
    char_counts = Counter(chars)
    total_length = 0

    for word in words:
      word_counts = Counter(word)
      # Check if chars has enough of each letter needed for word
      if all(word_counts[c] <= char_counts[c] for c in word_counts):
        total_length += len(word)

    return total_length