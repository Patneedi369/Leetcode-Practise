from collections import defaultdict
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = defaultdict(int)
        total_pairs = 0
        
        for d in dominoes:
            # Represent domino in a sorted/normalized form
            key = tuple(sorted(d))
            
            # Add existing count to total pairs, then increment count
            total_pairs += counts[key]
            counts[key] += 1
            
        return total_pairs