from collections import Counter

class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        # Count the frequency of each string while preserving original order
        counts = Counter(arr)
        
        # Iterate through the array to find distinct strings (frequency == 1)
        for s in arr:
            if counts[s] == 1:
                k -= 1
                if k == 0:
                    return s
                    
        return ""