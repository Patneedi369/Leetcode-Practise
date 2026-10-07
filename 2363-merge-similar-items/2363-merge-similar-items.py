from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        weights = defaultdict(int)
        
        # Aggregate weights for items in items1
        for value, weight in items1:
            weights[value] += weight
            
        # Aggregate weights for items in items2
        for value, weight in items2:
            weights[value] += weight
            
        # Return sorted result based on item values
        return [[value, weights[value]] for value in sorted(weights.keys())]